import streamlit as st
import asyncio
from io import BytesIO
from aiogtts import aiogTTS
from streamlit_extras.no_default_selectbox import selectbox

st.set_page_config(
    page_title="TTS",
    layout="wide",
    initial_sidebar_state="collapsed",
)


async def TTS():
    gtts = aiogTTS()
    if lang == "한국어":
        l = 'ko'
    elif lang == "영어":
        l = 'en'
    else:
        st.info("언어를 선택해 주세요.")
        return
    b = BytesIO()
    await gtts.write_to_fp(text=text, lang=l, fp=b)
    st.audio(b)
    st.download_button(label="다운로드", data=b, file_name=text+".mp3")


st.title("TTS")
text = st.text_area(label="TTS 오디오를 생성할 텍스트를 입력하세요.")
lang = selectbox(
    "언어를 선택해 주세요.",
    ["한국어", "영어"],
    no_selection_label="언어를 선택해 주세요."
)


def tts():
    asyncio.run(TTS())


st.button("TTS 오디오 생성", on_click=tts)
