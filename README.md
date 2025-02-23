
**YouTube Video to Blog Generator - README**

**📌 Project Overview**
The YouTube Video to Blog Generator is an AI-powered application that extracts transcripts from YouTube videos, rewrites them into well-structured blog articles, generates high-quality images, and provides an audio narration of the article. The application is built using Streamlit for an interactive web interface, OpenAI's GPT-4 for content generation, DALL·E 3 for image creation, and Google Text-to-Speech (gTTS) for converting text to audio.

**🚀 Features**
✅ YouTube Transcript Extraction – Automatically fetches video transcripts.
✅ AI-Powered Blog Generation – Converts raw transcripts into structured blog articles.
✅ DALL·E 3 Image Creation – Generates a unique, high-quality image for each blog post.
✅ Text-to-Speech Narration – Converts the blog post into an audio version.
✅ Streamlit Web Interface – User-friendly, interactive application.

**📂 Project Structure**

**📦 YouTube-Blog-Generator**
├── app.py                 # Main application script
├── requirements.txt       # List of required dependencies
├── README.md              # Documentation


**🛠 Technologies Used**

Streamlit 🎨	Web UI for the application
YouTube Transcript API 🎥	Extracts transcript from YouTube videos
OpenAI GPT-4 🤖	Generates well-structured blog articles
OpenAI DALL·E 3 🎨	Creates blog images based on the article title
Google Text-to-Speech (gTTS) 🎙️	Converts blog text into speech
Pillow 🖼️	Handles image processing
Requests 🌍	Fetches images from OpenAI APIs

**📜 File Descriptions**

**1️⃣ app.py (Main Application)**

Provides a Streamlit-based UI for users to input YouTube video URLs.
Extracts transcripts using the YouTube Transcript API.
Processes the transcript with GPT-4, generating structured blog articles.
Generates a relevant high-quality image using DALL·E 3.
Converts text into an audio file using gTTS.
Displays the title, subtitle, blog article, image, and audio playback in an intuitive interface.

**2️⃣ requirements.txt (Dependencies)**

Lists all required libraries:
streamlit: For building the UI.
youtube_transcript_api: To fetch YouTube video transcripts.
gtts: To convert text into speech.
openai: To generate blog content and images.
requests: To fetch images from OpenAI.
pillow: To handle image processing.

**🛠 Installation & Setup**

**1️⃣ Clone the Repository**

git clone https://github.com/Bealux007/YouTube-Blog-Generator.git
cd YouTube-Blog-Generator
**2️⃣ Create a Virtual Environment**

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
**3️⃣ Install Dependencies**

pip install -r requirements.txt
**4️⃣ Set Up API Keys**

OPENAI_API_KEY=your-api-key-here

**🚀 Running the Application**

Run the Streamlit Web App
streamlit run app.py
Open the generated local link.
Paste a YouTube video URL.
View the generated blog, image, and audio playback.


**🌟 How It Works**

**1️⃣ Extracting the Transcript**

Uses the YouTube Transcript API to fetch the transcript.
Cleans and structures the extracted text.
**2️⃣ Generating a Blog Article**

Uses GPT-4 to rewrite the transcript into a structured blog post.
Generates a title and subtitle for the blog.
**3️⃣ Creating an AI-Generated Image**

Uses DALL·E 3 to generate a high-quality blog image based on the blog title and subtitle.
**4️⃣ Converting the Blog to Speech**

Uses gTTS (Google Text-to-Speech) to create an audio narration of the blog.


**🔮 Future Improvements**

🔹 Enhance Speech-to-Text Accuracy – Improve handling of transcripts for better readability.
🔹 Expand Image Customization – Allow users to select different image styles.
🔹 Improve UI/UX – Enhance the web interface for a better user experience.
🔹 Multi-Language Support – Allow blog generation in multiple languages.

**📜 License**
This project is MIT Licensed.

**🔗 Contribute**
Pull requests are welcome! If you find a bug, open an issue.
