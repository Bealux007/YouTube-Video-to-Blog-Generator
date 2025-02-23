# load the necessary library and modules
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import openai
import re
import requests
from gtts import gTTS
from io import BytesIO
from PIL import Image
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY  # Set API key for OpenAI

# Extract YouTube video ID
def extract_video_id(youtube_url):
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", youtube_url)
    return match.group(1) if match else None

# Get transcript from YouTube
def get_youtube_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([t['text'] for t in transcript])
    except Exception as e:
        return f"Error retrieving transcript: {e}"

# Generate a spinned article using GPT-4
def generate_spinned_article(transcript):
    prompt = f"Rewrite the following YouTube transcript into a well-structured, engaging blog article with a creative title, subtitle, and key insights:\n\n{transcript}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert blogger."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=700
    )
    
    article = response["choices"][0]["message"]["content"]
    
    # Extract title and subtitle from article
    title_match = re.search(r"(?<=Title: )(.+)", article)
    subtitle_match = re.search(r"(?<=Subtitle: )(.+)", article)
    
    title = title_match.group(1) if title_match else "Untitled Blog"
    subtitle = subtitle_match.group(1) if subtitle_match else "No subtitle available."
    
    return title, subtitle, article

def generate_image(title):
    """Generate a high-quality image using OpenAI's DALL·E 3 model based on the blog title and subtitle."""
    
    prompt = (
        f"A stunning, high-quality blog image illustrating '{title}'. "
        f"The theme should match: '{subtitle}'. "
        "Use photorealistic details, beautiful lighting, and vibrant colors. "
        "Ensure the image looks cinematic, professional, and visually engaging."
    )

    response = openai.Image.create(
        model="dall-e-3",  # Upgrade to DALL·E 3
        prompt=prompt,
        n=1,
        size="1024x1024"  # Higher quality image
    )

    img_url = response["data"][0]["url"]
    img_response = requests.get(img_url)
    img = Image.open(BytesIO(img_response.content))

    return img


# Convert text to audio using Google Text-to-Speech
def text_to_speech(article):
    tts = gTTS(text=article, lang='en')
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    return audio_bytes

# Streamlit UI
st.title("YouTube Video to Blog Generator 📝🎙️")

youtube_url = st.text_input("Paste a YouTube video link here:")

if youtube_url:
    with st.spinner("Processing video..."):
        video_id = extract_video_id(youtube_url)
        if video_id:
            transcript = get_youtube_transcript(video_id)
            
            if "Error" not in transcript:
                title, subtitle, article = generate_spinned_article(transcript)
                image = generate_image(title)
                audio = text_to_speech(article)
                
                st.header(title)
                st.subheader(subtitle)
                
                if image:
                    st.image(image, caption="Generated Blog Image", use_container_width=True)
                
                st.write(article)
                
                # Display audio
                st.audio(audio.getvalue(), format="audio/mp3")
            else:
                st.error("Could not retrieve transcript. Please try another video.")
        else:
            st.error("Invalid YouTube URL. Please check and try again.")
