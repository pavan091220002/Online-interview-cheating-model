import pyttsx3
import datetime
import speech_recognition as sr
import openai

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

openai.api_key = "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"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("It is a fine morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your personal AI Assistant Dave! How can I be of service")

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("I could not get you, please speak again")
        return "None"
    return query

def get_openai_response(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    greet()
    while True:
        query = command().lower()
        if query != "none":
            speak("Let me think about that...")
            openai_response = get_openai_response(query)
            print("OpenAI Response:", openai_response)
            speak(openai_response)
