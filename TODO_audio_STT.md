# TODO: Add Audio Upload → Speech-to-Text → Scoring

- [ ] Backend: add `POST /api/score-audio` (multipart upload `audio`, optional `duration_seconds`)
- [x] Backend: save uploaded audio to `generated_outputs/` with unique absolute path

- [ ] Backend: Whisper transcription → `transcript`
- [ ] Backend: call existing `scorer.calculate_score()` + `generate_video_artifact()`
- [ ] Backend: return JSON compatible with UI (`overall_score`, `criteria_scores`, `metadata`, `generated_video`)
- [ ] Frontend (existing UI only): add file input + “Upload audio & score” button in transcript panel
- [ ] Frontend: JS `scoreAudio()` using `FormData` → `/api/score-audio`
- [ ] Frontend: populate textarea with extracted transcript + render existing results
- [ ] Dependencies: update `requirements.txt` to include Whisper (`openai-whisper`)
- [ ] Testing: run Flask, upload an audio sample, verify transcript + scoring + generated video

