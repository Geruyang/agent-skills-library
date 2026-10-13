# Scribe Transcription Pipeline

Use AI Services Scribe when the input is already a file or storage object and the output should be a transcript JSON payload or transcript files.

## Skill Chain

- Primary: [../../scribe/SKILL.md](../../x-openai-scribe-a8317f9/SKILL.md)
- Optional storage/download source: [../../rest-api/SKILL.md](../../x-openai-build-zoom-rest-api-app-fa8ade3/SKILL.md)
- Optional webhook hardening: [../../webhooks/SKILL.md](../../x-openai-setup-zoom-webhooks-e8837c7/SKILL.md)

## When to Use Scribe

Use `scribe` for:
- one uploaded file that should be transcribed immediately
- S3 archive transcription in the background
- post-processing exported media files into searchable transcript data

Do not use `scribe` for:
- live in-meeting media stream ingestion
- bot-style participant join and raw recording

For those, use:
- [../../rtms/SKILL.md](../../x-openai-zoom-rtms-ae86f57/SKILL.md) for live media streams
- [../../meeting-sdk/linux/SKILL.md](../../x-openai-zoom-meeting-sdk-linux-7c38d37/SKILL.md) for visible meeting bots

## Minimal Flow

```text
input file or storage prefix
  -> generate Build JWT
  -> choose fast mode or batch mode
  -> submit Scribe request
  -> receive transcript JSON or batch job state
  -> persist transcript output
```

## Typical Variants

1. Fast mode
   - one short file
   - immediate response needed
   - `POST /aiservices/scribe/transcribe`

2. Batch mode
   - long recordings or many files
   - `POST /aiservices/scribe/jobs`
   - monitor with polling or webhook notifications

3. Zoom recording re-transcription
   - use REST API to download or export recording files
   - feed those files into Scribe for your own transcript settings

## Common Failure Points

- wrong credential type (Build JWT vs normal OAuth token)
- choosing RTMS for offline archive transcription
- expired S3 credentials for batch jobs
- webhook signature verification implemented after JSON parsing instead of on raw body
