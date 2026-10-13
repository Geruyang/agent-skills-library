# Adapted from Agent Foundation docs/a13n-harness/getting-started.md.
# Copyright 2026 Converge AI. Apache-2.0; see ../LICENSE.
import asyncio
from collections.abc import AsyncIterator
from a13n_harness import AgentSpec, HarnessBuilder
from pydantic_ai.messages import ModelMessage
from pydantic_ai.models.function import AgentInfo, FunctionModel

async def respond(messages: list[ModelMessage], info: AgentInfo) -> AsyncIterator[str]:
    del messages, info
    yield "Hello from the Harness"

async def main() -> None:
    executable = HarnessBuilder().build(
        AgentSpec(), output_type=str, model=FunctionModel(stream_function=respond)
    )
    result = await executable.run("Say hello")
    print(result.output_or_raise())

if __name__ == "__main__":
    asyncio.run(main())
