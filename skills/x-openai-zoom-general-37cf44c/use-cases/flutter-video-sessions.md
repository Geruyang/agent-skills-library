# Flutter Video Sessions

Use this flow when you are building custom real-time video sessions in a Flutter mobile app.

## When to Use

- You need full control over UI/UX (not Zoom Meeting UI).
- You are building iOS/Android mobile session experiences in Flutter.
- You need helper-driven features such as chat, share, recording, or transcription.

## Skill Chain

1. [video-sdk/flutter](../../x-openai-zoom-video-sdk-flutter-3d5026c/SKILL.md)
2. [zoom-oauth](../../x-openai-zoom-oauth-13e78b7/SKILL.md)

## Typical Flow

1. Backend signs short-lived Video SDK JWT.
2. Flutter app initializes SDK and binds event listeners.
3. App joins session and activates media/helpers.
4. App leaves and cleans up explicitly.

## References

- [Flutter Video SDK Skill](../../x-openai-zoom-video-sdk-flutter-3d5026c/SKILL.md)
- [Lifecycle Workflow](../../x-openai-zoom-video-sdk-flutter-3d5026c/concepts/lifecycle-workflow.md)
- [Session Join Pattern](../../x-openai-zoom-video-sdk-flutter-3d5026c/examples/session-join-pattern.md)
