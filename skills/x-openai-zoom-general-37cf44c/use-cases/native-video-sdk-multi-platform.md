# Native Video SDK Multi-Platform Delivery

## Goal

Ship one product experience across Android, iOS, macOS, and Unity while keeping token auth, session behavior, and upgrade policies aligned.

## Skills to chain

- [zoom-video-sdk](../../x-openai-build-zoom-video-sdk-app-93497e9/SKILL.md)
- [zoom-video-sdk-android](../../x-openai-zoom-video-sdk-android-9271920/SKILL.md)
- [zoom-video-sdk-ios](../../x-openai-zoom-video-sdk-ios-a51b747/SKILL.md)
- [zoom-video-sdk-macos](../../x-openai-zoom-video-sdk-macos-a68d275/SKILL.md)
- [zoom-video-sdk-unity](../../x-openai-zoom-video-sdk-unity-de31698/SKILL.md)
- [zoom-oauth](../../x-openai-zoom-oauth-13e78b7/SKILL.md)

## Recommended delivery model

1. Standardize backend token service contract (`sessionName`, `userName`, role/claims).
2. Keep platform session state machines consistent (init -> join -> media -> leave).
3. Version-lock each platform release and run compatibility checks before rollout.
4. Maintain per-platform fallback plans for renamed/deprecated APIs.

## Failure modes to pre-plan

- Wrapper/native feature mismatch (especially Unity).
- Event naming drift across SDK versions.
- Token claim changes that break only one platform.
- Permission/regression differences per OS release.

## Output checklist

- Shared auth/token contract spec
- Platform-specific session lifecycle docs
- Upgrade runbook with rollback plan
- Known incompatibility matrix
