# Native Meeting SDK Multi-Platform Delivery

Use this flow when you need the same embedded meeting product capability across multiple native stacks (Android, iOS, macOS, Unreal) while keeping behavior and auth patterns consistent.

## When to Use

- You are shipping a shared meeting feature set across multiple native clients.
- You need consistent auth/signature and role policy across platforms.
- You need version-drift guardrails and staged rollout checks per platform.

## Skill Chain

1. [meeting-sdk](../../x-openai-build-zoom-meeting-sdk-app-f579820/SKILL.md)
2. [meeting-sdk/android](../../x-openai-zoom-meeting-sdk-android-4398669/SKILL.md)
3. [meeting-sdk/ios](../../x-openai-zoom-meeting-sdk-ios-0bffd09/SKILL.md)
4. [meeting-sdk/macos](../../x-openai-zoom-meeting-sdk-macos-cf65110/SKILL.md)
5. [meeting-sdk/unreal](../../x-openai-zoom-meeting-sdk-unreal-c2dabd5/SKILL.md)
6. [oauth](../../x-openai-zoom-oauth-13e78b7/SKILL.md)

## Typical Flow

1. Standardize server-side signing and role policy once.
2. Validate default UI join/start baseline on each platform.
3. Add platform-specific custom UI features only after baseline parity.
4. Maintain a version matrix and run upgrade checks per platform before release.
5. Track contradictions between wrapper docs, package artifacts, and API references.

## References

- [Meeting SDK Root Skill](../../x-openai-build-zoom-meeting-sdk-app-f579820/SKILL.md)
- [Android Reference Map](../../x-openai-zoom-meeting-sdk-android-4398669/references/android-reference-map.md)
- [iOS Reference Map](../../x-openai-zoom-meeting-sdk-ios-0bffd09/references/ios-reference-map.md)
- [macOS Reference Map](../../x-openai-zoom-meeting-sdk-macos-cf65110/references/macos-reference-map.md)
- [Unreal Reference Map](../../x-openai-zoom-meeting-sdk-unreal-c2dabd5/references/unreal-reference-map.md)
