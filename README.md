# YouTube Transcript → Detailed Notes (Gemini-powered)
Turn any YouTube video's transcript into concise, structured, and useful notes using Google Gemini (GenAI) and a tiny Streamlit app.

TL;DR: paste a YouTube link, provide your Gemini API key, and the app fetches the video transcript, summarizes the content into actionable bullet points (≤ 250 words), and displays the result in an easy-to-read format.

---

## Features
- One-file Streamlit web UI: easy to run and modify (`app.py`).
- Automatically fetches transcripts via youtube-transcript-api.
- Summarizes long transcripts using Google Gemini (GenAI) model.
- Shows YouTube thumbnail for quick context.

---

## Stack
- Language: Python (3.9+ recommended)
- Runtime: Streamlit (web UI)
- Notable libraries:
  - youtube_transcript_api — fetches video transcripts
  - google-genai — Gemini client for LLM generation
  - streamlit — lightweight UI and deployment

Files you’ll care about:
- `app.py` — main Streamlit app (UI, transcript extraction, Gemini call)
- `requirements.txt` — dependencies
- `LICENSE` — repository license

---

## Quickstart — Run locally (recommended)
1. Clone the repo:
   git clone https://github.com/mdzaheerjk/End-To-End-Youtube-Video-Transcribe-Summarizer-LLM-App-With-Google-Gemini-Pro.git
   cd End-To-End-Youtube-Video-Transcribe-Summarizer-LLM-App-With-Google-Gemini-Pro

2. Create and activate a virtual environment (optional but recommended):
   python -m venv .venv
   source .venv/bin/activate  # macOS / Linux
   .venv\Scripts\activate     # Windows (PowerShell)

3. Install dependencies:
   pip install -r requirements.txt

4. Set your Google Gemini API key (example):
   export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"     # macOS / Linux
   setx GEMINI_API_KEY "YOUR_GEMINI_API_KEY"      # Windows (restart required)

   Note: The app's UI asks for the Gemini API key in the sidebar — you can paste it there instead of using env vars.

5. Run the app:
   streamlit run app.py

6. In the Streamlit UI:
   - Paste a YouTube video link (e.g., https://www.youtube.com/watch?v=VIDEO_ID)
   - Click "Get Deatiled Notes"
   - The app will fetch the transcript, send it to Gemini, and display a bullet-point summary.

---

## How it works (high level)
1. User provides a YouTube link in the Streamlit UI.
2. The app extracts the `video_id` from the link and uses `youtube_transcript_api` to fetch the transcript snippets.
3. Snippets are concatenated into a single transcript string.
4. The transcript is sent to the Google Gemini model via `google-genai` with a summarization prompt.
5. Gemini returns a concise summary (the app currently requests ~250-word bullet summary); Streamlit renders the result.

Key functions (see `app.py`):
- `extract_transcription_details(youtube_video_url)` — obtains the transcript text.
- `generate_gemini_content(transcript_text, prompt)` — calls Gemini to produce the summary.

---

## Configuration & environment
- GEMINI API key: obtained from your Google Cloud / Gemini account. The app asks for it in the sidebar (password input).
- YouTube transcripts: videos must have transcripts available (auto-generated transcripts are often available; some videos may not provide transcripts).

Environment variables you may use (optional):
- GEMINI_API_KEY — if you prefer to avoid typing the key into the UI.

---

## Usage notes & tips
- Long transcripts: Gemini models have input size limits. For very long videos (multiple hours), consider pre-chunking the transcript and summarizing per-chunk, then combining summaries.
- Rate limits & costs: calling Gemini may incur costs — keep prompts concise and batch when appropriate.
- Transcript availability: not all videos have transcripts. When `youtube_transcript_api` cannot find one, it will raise an error displayed by Streamlit.

---

## Possible improvements (ideas)
- Add transcript chunking + hierarchical summarization to handle long videos safely within model context windows.
- Add caching for transcripts and summaries (disk or Redis) to avoid repeated downloads / API calls.
- Provide model selection and temperature sliders in the UI.
- Add export options: PDF, Markdown, or downloadable text files.
- Better error handling: clearer messages for missing transcripts, invalid links, or API failures.

---

## Troubleshooting
- "Transcript not found" — some videos block transcripts or are community/region-restricted.
- "Gemini API error" — verify your API key, account access, and quota.
- Streamlit UI looks broken — ensure you installed the correct `streamlit` version and are running the app with a compatible Python interpreter (3.9+ recommended).

---

## Example
1. Enter: https://www.youtube.com/watch?v=dQw4w9WgXcQ
2. The app will show the thumbnail and output a structured, ~250-word set of bullet points summarizing the content.

---

## Contributing
Contributions welcome! Suggestions:
- Open an issue describing the enhancement or bug.
- Fork, add tests and improvements, and open a PR.

If you’d like me to:
- Add chunked summarization code and a sample implementation, say "Please add chunked summarization".
- Commit this README.md for you — tell me to proceed and confirm the repo target.

---

## License
This repository includes `LICENSE`. Check it for details and attribution.

---
Acknowledgements: built with Streamlit, youtube-transcript-api, and Google Gemini (google-genai).
