import streamlit as st
from gtts import gTTS
from newspaper import Article
from io import BytesIO
import base64

st.title("Text to Speech Converter")

# User input
input_type = st.radio("Choose Input Type", ("Text", "URL"))
language = 'en'  # English
text = ""  # Initialize text variable  # Initialize URL variable
ar_text = ""
if input_type == "Text":
    text = st.text_area("Enter the text you want to convert to speech")
    # Conversion to audio for text
    if st.button("Convert Text to Speech"):
        if text.strip():
            tts = gTTS(text=text, lang=language,tld='co.in', slow=False)
            audio_file = BytesIO()
            tts.write_to_fp(audio_file)

            # Option to save the audio
            st.audio(audio_file, format="audio/mp3")
            # encoding the audio file for saving
            audio_data = audio_file.getvalue()
            audio_data_base64 = base64.b64encode(audio_data)
            st.markdown(
                f'<a href="data:audio/mp3;base64,{audio_data_base64.decode()}" download="converted_text.mp3">Download Audio</a>',
                unsafe_allow_html=True)

            st.success("Conversion complete!")
        else:
            st.warning("No text to speak. Please enter some text or provide a valid article URL.")
else:
    article_url = st.text_input("Enter the URL of the article")
    if article_url == "":
        print("provide an article url")
    else:
        article = Article(article_url)
        article.download()
        article.parse()
        ar_text = article.text
    if st.button("Show Article"):
        st.write("Article Text :", ar_text)
    if st.button("Convert Article to Speech"):
        # Conversion to audio for fetched article
        if ar_text.strip():
            tts = gTTS(text=ar_text, lang=language,tld='co.in', slow=False)

            audio_file = BytesIO()
            tts.write_to_fp(audio_file)
            # Option to play the audio
            st.audio(audio_file, format="audio/mp3")

            # encoding the audio file for saving
            audio_data = audio_file.getvalue()
            audio_data_base64 = base64.b64encode(audio_data)
            st.markdown(
                f'<a href="data:audio/mp3;base64,{audio_data_base64.decode()}" download="converted_article.mp3">Download Audio</a>',
                unsafe_allow_html=True)

            st.success("Conversion complete!")
        else:
            st.warning("No article fetched. Please provide a valid article URL and fetch the article.")











