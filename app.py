import streamlit as st
from google import genai

from youtube_transcript_api import YouTubeTranscriptApi


st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter Gemini API Key",type='password')


prompt="""
You are Yotube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:  
"""


def extract_transcription_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("v=")[1].split("&")[0]

        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)

        transcript_text = " ".join(
            snippet.text for snippet in transcript
        )

        return transcript_text

    except Exception as e:
        st.error(e)
        return None

def generate_gemini_content(transcript_text, prompt):
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt + transcript_text,
    )

    return response.text
st.title("Youtube Transcript to Detailed Notes Converter")
youtbe_link=st.text_input("Enter Youtube Video Link:")

if youtbe_link:
    video_id = youtbe_link.split("v=")[1].split("&")[0]
    print(video_id)

    st.image(
    f"https://img.youtube.com/vi/{video_id}/0.jpg",
    use_container_width=True
    )

if st.button("Get Deatiled Notes"):
    transcript_text=extract_transcription_details(youtbe_link)

    if transcript_text:
        summary=generate_gemini_content(transcript_text,prompt)
        st.markdown('## Deatiled Notes:')
        st.write(summary)