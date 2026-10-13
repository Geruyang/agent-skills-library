"""Rebuild bounded provenance indexes from this download bundle, never user config."""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

SKILL = Path(__file__).resolve().parents[1]

# Authored synthesis with exact snapshot-local source entrypoints.
NOTES = {
    'openai/codex': ('coding-runtime', 'Rust runtime 与 app-server 协议分离；审批、工具执行、rollout 各有边界。参考完整编码产品，不把内部 API 当稳定跨宿主协议。', ['codex-rs/app-server/README.md', 'codex-rs/core/src/tools/approvals.rs', 'codex-rs/core/src/rollout.rs']),
    'anthropics/claude-code': ('product-integration', '公开仓库主要用于文档、插件与示例，不等于完整产品运行时开源；根许可证指向商业条款。SDK 和产品许可分开判断。', ['LICENSE.md', 'plugins/README.md']),
    'bytedance/trae-agent': ('coding-runtime', 'Python 研究友好循环、工具执行器和 trajectory；适合消融及自研实验，不代表 TRAE IDE 整体源码。', ['trae_agent/agent/base_agent.py', 'trae_agent/utils/trajectory_recorder.py']),
    'lencx/ChatGPT': ('desktop-shell', 'Tauri webview/IPC 桌面封装；v2-dev 无根许可证文件，不能默认允许复制；不提供通用可靠 agent 平台。', ['src-tauri/src/main.rs']),
    'anomalyco/opencode': ('coding-runtime', '按 session key 串行协调、不同 key 并发；interrupt 接受与 cleanup 完成不同，wake 防丢唤醒。与同名 Go 归档仓库不同。', ['packages/core/src/session/run-coordinator.ts', 'packages/core/src/permission.ts']),
    'google-gemini/gemini-cli': ('coding-runtime', '工具 scheduler 显式跟踪验证、审批、执行和终态；sandbox 与 checkpoint 分层，适合观察可取消工具队列。', ['packages/core/src/scheduler/state-manager.ts', 'docs/cli/sandbox.md', 'docs/cli/checkpointing.md']),
    'earendil-works/pi': ('embedded-runtime', 'AgentMessage 到提供方消息的转换在调用边界；steering/followup 和扩展可组合，小核心不自动提供平台持久调度。', ['packages/agent/src/agent-loop.ts', 'packages/coding-agent/docs/sdk.md']),
    'Aider-AI/aider': ('context-coding', 'RepoMap 用代码 tag/缓存与 token 预算选择上下文；编辑和 Git 流程适合编码助手，不等同通用服务编排。', ['aider/repomap.py', 'aider/coders/base_coder.py']),
    'aaif-goose/goose': ('coding-runtime', '持久会话上的 re-entrant operation pipeline；整批工具请求须全部配对，单个 tool result 不能代表批次结束。', ['crates/goose/src/agents/state_machine/mod.rs', 'crates/goose/src/agents/extension_manager/mod.rs']),
    'LibreChat-AI/LibreChat': ('chat-platform', '产品层多 agent、认证和持久 checkpoint；graph namespace 与存储 owner scope 有区别，租户/代际归属需显式保存。', ['packages/api/src/agents/checkpointer.ts', 'api/server/services/PermissionService.js']),
    'CherryHQ/cherry-studio': ('desktop-platform', 'renderer IPC、主进程流管理、持久化分层；主进程为审批单写者，attach/detach/abort 语义区分。许可 AGPL 需按复用组件检查。', ['docs/references/ai/core-architecture.md', 'docs/references/ai/tool-approval.md']),
    'cline/cline': ('coding-runtime', 'SDK 核心将 host、会话、待决 prompt、automation 服务装配到多种客户端，复用时查 runtime capability 和产品版本。', ['sdk/packages/core/src/ClineCore.ts']),
    'lobehub/lobehub': ('chat-platform', 'Agent 与执行 engine 分离；executor 可覆盖、human interaction 与 group orchestration 明确建模。社区许可证不能当普通 MIT。', ['packages/agent-runtime/src/core/runtime.ts', 'packages/agent-runtime/src/groupOrchestration/GroupOrchestrationRuntime.ts']),
    'open-webui/open-webui': ('chat-platform', '多模型/检索/工具/权限的产品集成，中间件处理消息和工具；前端产品并不替代安全执行环境。使用其专有根许可。', ['backend/open_webui/utils/middleware.py']),
    'anthropics/skills': ('skill-library', '技能流程、资源与可验收产物；MCP builder 强调契约和评估。docx/pdf/pptx/xlsx 为 source-available，按组件许可。', ['skills/mcp-builder/SKILL.md', 'skills/skill-creator/SKILL.md']),
    'anthropics/claude-plugins-official': ('plugin-library', '插件装配 skills/commands/agents/hooks/MCP；名称 slug 不宜随意更改；市场收录不代表权限与兼容性已验证。', ['plugins/mcp-server-dev/skills/build-mcp-server/references/tool-design.md']),
    'openai/plugins': ('plugin-library', '下载技能和 MCP 的最大来源；声明式装配业务知识与执行能力，云端连接定义不等于 SaaS 实现源码。', ['plugins/figma/README.md', 'plugins/data-analytics/src/analytics-app/handoff.mjs']),
    'openai/skills': ('skill-library', '标准技能包与分场景资源；保留工具/运行时要求，跨宿主按实际能力映射，不能仅替换产品名。', []),
    'obra/superpowers': ('workflow-methods', '分阶段计划、调试、验证、评审可按需吸收；不继承强制全局启动规则或隐式扩大派发/审批。', ['skills/using-superpowers/SKILL.md', 'skills/systematic-debugging/SKILL.md', 'skills/verification-before-completion/SKILL.md']),
    'muratcankoylan/Agent-Skills-for-Context-Engineering': ('context-methods', '上下文预算、压缩、长期记忆、评估、harness 与多 agent 隔离；高级 KV/cache 与自改进方法必须确认运行时条件。', ['skills/context-compression/SKILL.md', 'skills/multi-agent-patterns/SKILL.md', 'skills/evaluation/SKILL.md', 'skills/tool-design/SKILL.md']),
    'openai/openai-agents-python': ('agent-sdk', 'Agent/Runner、handoff、session/run state 与工具 guardrails；链首/链尾检查并不覆盖所有副作用，按工具边界控制。', ['docs/agents.md', 'docs/guardrails.md', 'docs/handoffs.md', 'src/agents/run_state.py']),
    'openai/openai-agents-js': ('agent-sdk', 'TypeScript runner、approval 与可恢复 RunState；序列化和工具 identity/version 耦合，不能假设与 Python 所有特性对称。', ['packages/agents-core/src/runState.ts', 'packages/agents-core/src/runner/runLoop.ts']),
    'anthropics/claude-agent-sdk-python': ('agent-sdk', '包装 Claude CLI；allowed_tools 是 auto-approve，can_use_tool 只处理 ask，PreToolUse 与 tools/disallowed_tools 各有语义。', ['src/claude_agent_sdk/types.py', 'src/claude_agent_sdk/query.py']),
    'OpenHands/software-agent-sdk': ('agent-sdk-server', 'Conversation/event store/security/workspace 与 Agent Server；IDLE 非终态，risk 分析与确认策略分离。调度由外部 automation 项目负责。', ['openhands-sdk/openhands/sdk/conversation/state.py', 'openhands-sdk/openhands/sdk/security/confirmation_policy.py']),
    'OpenHands/OpenHands': ('agent-ui', '当前快照是 Agent Canvas 前端，消费 SDK/Agent Server，不直接执行动作或提供隔离，automation 是独立服务。', ['docs/architecture.md']),
    'OpenHands/OpenHands-CLI': ('historical-cli', 'README 声明不再积极维护；可参考 ACP/local/remote runner，但新项目优先核验维护中入口。', ['openhands_cli/tui/core/conversation_runner.py']),
    'modelcontextprotocol/typescript-sdk': ('protocol-sdk', 'main 为 v2 分包；v1 import 路径与协议版本需分别匹配，避免把旧插件示例混用进新 SDK。', ['packages/server/README.md', 'packages/client/README.md']),
    'modelcontextprotocol/servers': ('mcp-reference', '七个 reference server 为教学实现；有工具不等于生产安全，roots 不能扩大初始允许范围。', ['src/filesystem/server.ts', 'src/everything/docs/architecture.md']),
    'ag-ui-protocol/ag-ui': ('ui-protocol', '事件/状态协议连接 agent 与 UI；按版本处理 snapshot/delta、顺序及 conformance，协议本身不执行业务或鉴权。', ['docs/concepts/architecture.mdx', 'sdks/typescript/packages/core/src/generated/types.ts']),
    'agentskills/agentskills': ('skill-format', 'SKILL.md frontmatter 与渐进披露规范；可移植目录不意味着宿主支持所有扩展字段和依赖。', ['docs/specification.mdx']),
    'continuedev/continue': ('historical-cli', 'README 标停止维护/只读；permissions 文档提示 headless 与 TUI 默认不同，应显式策略而非借用默认。', ['extensions/cli/src/permissions/README.md']),
    'RooCodeInc/Roo-Code': ('coding-runtime', 'CLI 从 ask/say 消息区分等待、完成、可恢复与输出；checkpoint 与执行状态分开，不能把部分流当终态。', ['apps/cli/docs/AGENT_LOOP.md', 'src/services/checkpoints/ShadowCheckpointService.ts']),
    'opencode-ai/opencode': ('historical-cli', '已归档的 Go/Bubble Tea 产品，指向 Crush；权限服务与 session approval 是历史设计参考，非 anomalyco OpenCode。', ['internal/permission/permission.go']),
    'openai/openai-chatkit-advanced-samples': ('ui-samples', 'FastAPI + React 示例，widget action 与服务端业务状态结合；示例 store/账号流程需要生产实现替换。', ['examples/customer-support/backend/app/server.py', 'examples/customer-support/backend/app/support_agent.py']),
    'converge-ai-labs/agent-foundation': ('harness-service', 'Harness 定义与 fresh RunBindings、状态恢复分开；Service 提供平台边界，UI 不等于 HTTP SDK；总树预算由宿主聚合。', ['docs/a13n-harness/agents-and-runs.md', 'docs/a13n-harness/mcp.md', 'deploy/docker/compose/README.md']),
}

TOPICS = {
    'architecture': ['agent','architecture','harness','orchestrat','workflow','design system'],
    'context-memory': ['context','memory','retrieval','rag','compression','knowledge'],
    'tools-protocol': ['mcp','tool','api','connector','integration'],
    'evaluation-quality': ['evaluat','test','debug','review','verif','benchmark'],
    'ui-artifacts': ['design','ui','visual','image','video','audio','slide','document','pdf','spreadsheet'],
    'deployment-platform': ['deploy','cloud','docker','kubernetes','infra','hosting'],
    'domain-workflow': ['customer','meeting','finance','marketing','support','crm','project'],
}

MCP_PURPOSES = {
    'airtable':'表格 数据库 records table database', 'atlassian-rovo':'项目 文档 搜索 Jira Confluence project search',
    'xcodebuildmcp':'iOS macOS 编译 模拟器 build simulator Xcode', 'canva':'设计 图片 visual design image',
    'clickup':'任务 项目 task project', 'cloudflare-api':'云 边缘 网络 cloud edge infrastructure',
    'codex-security':'安全 代码 审计 security code scan', 'consensus':'研究 学术 论文 research paper',
    'creative_production_mcp':'创意 媒体 图片 视频 creative media image video production',
    'creative-production':'创意 媒体 图片 视频 creative media image video production',
    'dataAnalyticsWidgets':'数据 分析 图表 可视化 chart visualization visual data analytics widgets',
    'data-analytics':'数据 分析 图表 可视化 chart visualization visual data analytics widgets',
    'datadog':'监控 日志 指标 monitoring logs metrics', 'dropbox':'文件 云盘 file storage',
    'figma':'界面 设计 原型 UI design prototype', 'github':'代码 仓库 issue pull request repository',
    'gmail':'邮件 email mail', 'google-calendar':'日程 日历 schedule calendar', 'google-drive':'云盘 文档 file document storage',
    'granola':'会议 笔记 meeting notes', 'higgsfield':'媒体 视频 图像 media video image',
    'linear':'项目 任务 issue project task', 'monday-com':'项目 工作流 project workflow',
    'notion':'文档 知识 笔记 document knowledge notes', 'openai-api-key-local-confirmation':'密钥 本地 确认 表单 key local confirmation elicitation',
    'posthog':'产品 分析 事件 product analytics event', 'sentry':'错误 监控 error monitoring',
    'shopify':'电商 商店 订单 ecommerce shop order', 'slack':'团队 消息 chat message team',
    'stripe':'支付 账单 payment billing', 'supabase':'数据库 后端 database backend', 'vercel':'网站 部署 web deployment',
    'zoom':'会议 meeting video', 'context7':'文档 查询 library documentation lookup',
    'discord':'聊天 社区 机器人 chat community bot', 'fakechat':'本地 测试 聊天 channel local test chat',
    'firebase':'后端 数据库 应用 backend database app', 'gitlab':'代码 仓库 CI issue repository',
    'imessage':'消息 macOS message', 'laravel-boost':'PHP Laravel 开发 development',
    'playwright':'浏览器 网页 自动化 browser web automation', 'serena':'代码 语义 符号 code semantic symbol LSP',
    'telegram':'消息 机器人 message bot', 'terraform':'基础设施 注册表 infrastructure registry IaC',
    'example-server':'示例 example template', 'everything':'协议 测试 示例 protocol test example',
    'filesystem':'文件 目录 读写 file directory read write', 'fetch':'网页 HTTP 内容 web content retrieval',
    'git':'版本 仓库 差异 version repository diff', 'memory':'记忆 知识 图谱 memory knowledge graph',
    'sequentialthinking':'步骤 思考 记录 sequential thinking steps', 'time':'时间 时区 time timezone',
}

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def load(p: Path):
    return json.loads(p.read_text(encoding='utf-8-sig'))

def write(p: Path, data):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def bundle_path(raw: str) -> str:
    normalized = raw.replace('\\','/')
    for marker in ('/code/', '/export/', '/reports/'):
        if marker in normalized:
            return marker.strip('/') + '/' + normalized.split(marker,1)[1]
    if normalized.startswith(('code/','export/','reports/')):
        return normalized
    raise ValueError('Not a downloaded bundle path: ' + normalized)

def main():
    if hasattr(sys.stdout,'reconfigure'): sys.stdout.reconfigure(encoding='utf-8')
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--root', type=Path, required=True); args=ap.parse_args()
    root=args.root.resolve(); original=load(root/'reports/source-download-manifest.json')['repositories']
    raw_by_repo={x['requested_repo']:x for x in original}
    if set(raw_by_repo) - set(NOTES):
        raise ValueError('New repository needs human synthesis: '+str(set(raw_by_repo)-set(NOTES)))
    foundation=load(root/'export/custom-skills/agent-foundation/references/provenance.json')
    raw_by_repo['converge-ai-labs/agent-foundation']={'commit':foundation['commit'], 'local_license':'Apache-2.0'}
    sources=[]; missing=[]
    for repo,(category,note,paths) in NOTES.items():
        p=root/'code'/repo; raw=raw_by_repo[repo]
        commit=subprocess.check_output(['git','-C',str(p),'rev-parse','HEAD'],text=True).strip()
        if commit != raw['commit']: raise ValueError('Snapshot drift: '+repo)
        tracked=subprocess.check_output(['git','-C',str(p),'ls-files'],text=True).splitlines()
        actual=['README.md']+paths
        evidence=[]
        for rel in dict.fromkeys(actual):
            f=p/rel
            if not f.is_file(): missing.append(repo+'/'+rel); continue
            data=f.read_bytes()
            evidence.append({'path':'code/'+repo+'/'+rel,'sha256':sha(data),'bytes':len(data)})
        licenses=[]
        for rel in tracked:
            if '/' not in rel and re.match(r'(?i)^(license|licence|copying|notice)(\.|$)',rel):
                f=p/rel
                if f.is_file(): licenses.append({'path':'code/'+repo+'/'+rel,'sha256':sha(f.read_bytes())})
        label=raw.get('local_license') or raw.get('license_summary') or raw.get('license',{})
        if isinstance(label,dict): label=label.get('name','Per-component; inspect files')
        sources.append({'id':repo,'url':'https://github.com/'+repo,'commit':commit,'category':category,'design_use':note,
                        'root':'code/'+repo,'license_summary':label,'license_files':licenses,'tracked_files':len(tracked),
                        'evidence':evidence,'verification':'selected source/document inspection; whole application not run'})
    manifest=load(root/'reports/skills-export-manifest.json'); skills=[]
    for row in manifest:
        if not row['origin'].startswith('upstream/'): raise ValueError('Non-download skill rejected')
        repo=row['origin'].removeprefix('upstream/')
        if repo not in NOTES: raise ValueError('Unknown skill repository')
        rel='export/skills/'+row['id']+'/SKILL.md'; p=root/rel; data=p.read_bytes(); body=data.decode('utf-8-sig')
        fm=body.split('---',2)[1] if body.startswith('---') else ''
        match=re.search(r'^description:\s*(.*(?:\n[ \t]+.*)*)',fm,re.M)
        description=' '.join(match.group(1).strip().strip('\"\'').split()) if match else ''
        text=(row['original_name']+' '+description+' '+body).lower()
        topics=[k for k,words in TOPICS.items() if any(w in text for w in words)] or ['domain-workflow']
        source=bundle_path(row['source'])
        # Component licenses remain authoritative; root license alone may not cover this skill.
        license_paths=[]
        for parent in [p.parent, root/source]:
            if parent.is_dir():
                license_paths.extend(f.relative_to(root).as_posix() for f in parent.iterdir() if f.is_file() and re.match(r'(?i)^(license|licence|notice)',f.name))
        skills.append({'id':row['id'],'name':row['original_name'],'repository':repo,'source':source,'path':rel,
                       'sha256':sha(data),'description':description,'topics':topics,'component_license_paths':sorted(set(license_paths)),
                       'integration':'retrieve on demand; inspect body, dependencies and component terms before use'})
    cat=load(root/'export/mcp/upstream-catalog/inventory.json'); prov=load(root/'export/mcp/provenance.json')
    mcps=[]
    for i,row in enumerate(cat['entries']):
        mcps.append({'id':'definition-'+str(i+1),'name':row['name'],'kind':'catalog-definition','source':bundle_path(row['source']),
                     'source_sha256':row.get('source_sha256'),'transport':row.get('transport'), 'status':row.get('status'),
                     'installation_status':row.get('installation_status'),'requirements':row.get('requirements_zh') or row.get('reason'),
                     'verification':'historical source catalog; business/UI authorization not inferred'})
    for row in prov['servers']:
        mcps.append({'id':'local-'+row['name'],'name':row['name'],'kind':'local-implementation','source':bundle_path(row['source']),
                     'path':bundle_path(row['export']),'source_commit':row.get('source_commit'),'status':row.get('status'),
                     'tools_count':row.get('tools_count'),'adaptation':row.get('adaptation'),
                     'verification':'historical per-server evidence; not a new runtime test'})
    for name,row in prov.get('catalog_followup',{}).items():
        if row.get('status') != 'installed_local': continue
        mcps.append({'id':'local-'+name,'name':name,'kind':'local-implementation',
                     'source':bundle_path(row['sources'][0]), 'status':row['status'],
                     'requirements':row.get('requirements'), 'launcher':'export/mcp/additional_launch.py',
                     'verification':'historical additional installation; business prerequisites remain separate'})
    for row in mcps:
        row['purpose_keywords']=MCP_PURPOSES.get(row['name'],'')
        if not row['purpose_keywords']: raise ValueError('MCP purpose needs human classification: '+row['name'])
    locks=[]
    lock_paths=list((root/'export/mcp/locks').iterdir())
    lock_paths.extend(root/'export/mcp'/rel for rel in prov.get('official_dependency_locks',[]))
    for rel in ['runtime/portable-node/LICENSE.txt','runtime/portable-python/LICENSE.txt','runtime/python-requirements.lock.txt']:
        if (root/'export/mcp'/rel).is_file(): lock_paths.append(root/'export/mcp'/rel)
    for p in sorted(set(lock_paths)):
        if not p.is_file(): continue
        locks.append({'path':p.relative_to(root).as_posix(),'sha256':sha(p.read_bytes()),
                      'role':'Runtime lock/license/build evidence; installed dependency, not an additional reviewed repository'})
    write(SKILL/'references/runtime-dependencies.json',locks)
    followup=load(root/'export/mcp/upstream-catalog/remaining-41.json')
    followup_rows=[{k:row.get(k) for k in ('name','purpose','requirements','installation_status','sources','official_docs')} for row in followup['entries']]
    write(SKILL/'references/mcp-followup.json',{'original_remaining':followup['original_remaining'],'remaining_not_enabled':followup['remaining_not_enabled'],'entries':followup_rows})
    write(SKILL/'references/source-index.json',sources); write(SKILL/'references/skill-index.json',skills); write(SKILL/'references/mcp-index.json',mcps)
    report={'created_at':datetime.now(timezone.utc).isoformat(),'scope':'Downloaded bundle only; no personal skills/config/credentials read',
            'repositories_expected':len(raw_by_repo),'repositories_covered':len(sources),'skills_expected':len(manifest),'skills_covered':len(skills),
            'skill_source_counts':dict(Counter(x['repository'] for x in skills)),'mcp_definitions_expected':cat['definitions'],
            'mcp_definitions_covered':sum(x['kind']=='catalog-definition' for x in mcps),'mcp_unique_catalog_targets':cat['unique_endpoints_or_launches'],
            'mcp_local_implementations':sum(x['kind']=='local-implementation' for x in mcps),'runtime_dependency_locks':len(locks),'selected_evidence_files':sum(len(x['evidence']) for x in sources),
            'missing_curated_paths':missing,'coverage_limits':['All entries indexed; not all source lines reviewed','All exported skill bodies read for classification/hash; specialized workflows not all executed','Source-level synthesis is distinct from historical/runtime verification'],
            'remaining_mcp_followup_entries':len(followup_rows),'remaining_mcp_not_enabled':followup['remaining_not_enabled'],
            'supplemental_authored_skill':{'path':'export/custom-skills/agent-foundation/SKILL.md','sha256':sha((root/'export/custom-skills/agent-foundation/SKILL.md').read_bytes())},
            'passed':not missing and len(skills)==667 and len(sources)==35 and cat['definitions']==45 and sum(x['kind']=='local-implementation' for x in mcps)==16}
    write(root/'reports/agent-designer-coverage.json',report)
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
