# React Native Video Sessions

Use this flow for custom mobile video session products in React Native.

## When to Use

- You need full custom UX (not Zoom Meeting UI).
- You are building iOS/Android apps using `@zoom/react-native-videosdk`.
- You need helper-based features such as chat/share/recording/transcription.

## Skill Chain

1. [video-sdk/react-native](../../x-openai-zoom-video-sdk-react-native-bf16e19/SKILL.md)
2. [zoom-oauth](../../x-openai-zoom-oauth-13e78b7/SKILL.md)

## Typical Flow

1. Backend signs short-lived Video SDK JWT.
2. App initializes SDK provider and listeners.
3. App joins session with tokenized config.
4. App drives helper APIs and event-based UI state.
5. App leaves session and cleans up resources.

## References

- [React Native Video SDK Skill](../../x-openai-zoom-video-sdk-react-native-bf16e19/SKILL.md)
- [Lifecycle Workflow](../../x-openai-zoom-video-sdk-react-native-bf16e19/concepts/lifecycle-workflow.md)
- [Session Join Pattern](../../x-openai-zoom-video-sdk-react-native-bf16e19/examples/session-join-pattern.md)
