import streamlit as st
from io import BytesIO
from gtts import gTTS
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

st.set_page_config(
    page_title="TTS",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def tts():
    lang = detect(text)
    gtts = gTTS(text=text, lang=lang)
    b = BytesIO()
    gtts.write_to_fp(b)
    st.audio(b)
    st.download_button(label="다운로드", data=b, file_name=text+".mp3")
    return


st.title("TTS")
text = st.text_area(label="TTS 오디오를 생성할 텍스트를 입력하세요.")

st.button("TTS 오디오 생성", on_click=tts)