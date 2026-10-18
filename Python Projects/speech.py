
import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone(device_index=0) as source:
    print("Adjusting for background noise...")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Listening... speak now")

    try:
        audio_data = recognizer.listen(
            source, timeout=5, phrase_time_limit=15
        )
        text = recognizer.recognize_google(audio_data)
        print(f"Transcription: {text}")

    except sr.WaitTimeoutError:
        print("No speech detected. Please try again.")
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
    except sr.RequestError as e:
        print(f"Google Speech Recognition error: {e}")
