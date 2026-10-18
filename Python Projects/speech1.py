
import streamlit as st
import speech_recognition as sr
import io

st.set_page_config(page_title="Speech to Text", page_icon="🎙️")
st.title("🎙️ Speech to Text")
st.write("Record your voice and convert it into text.")

languages = {
    "English": "en-IN",
    "Hindi": "hi-IN",
    "Malayalam": "ml-IN",
    "Kannada": "kn-IN",
}

lang_name = st.selectbox("Choose a language:", list(languages.keys()))
recorded = st.audio_input("🎤 Click the microphone and speak")

if st.button("Convert to Text", type="primary"):
    if recorded is None:
        st.warning("Please record some audio first.")
    else:
        with st.spinner("Transcribing your audio..."):
            try:
                recognizer = sr.Recognizer()

                # Convert recorded audio to a readable WAV file
                audio_bytes = recorded.getvalue()

                with sr.AudioFile(io.BytesIO(audio_bytes)) as source:
                    audio_data = recognizer.record(source)

                text = recognizer.recognize_google(
                    audio_data,
                    language=languages[lang_name]
                )

                st.success("Transcription completed!")
                st.text_area("Your transcription:", value=text, height=150)

                st.download_button(
                    "Download Transcription",
                    data=text,
                    file_name="transcription.txt",
                    mime="text/plain",
                )

            except sr.UnknownValueError:
                st.error("Speech not understood. Please record again.")
            except sr.RequestError as e:
                st.error(f"Speech recognition service error: {e}")
            except Exception as e:
                st.error(f"Error: {e}")
