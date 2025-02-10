import requests
import pyttsx3
import speech_recognition as sr

# Initialize the text-to-speech engine
engine = pyttsx3.init()

key ="AIzaSyA7-DIy80ZupxsXcMaCSDZdfwu-i4IJLvM"

def speak(text):
    """Convert text to speech."""
    # engine.setProperty('voice', voices)
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    """Recognize speech using the microphone."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("Processing...")
            query = recognizer.recognize_google(audio)
            return query
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that.")
        except sr.RequestError:
            speak("There seems to be an issue with the speech recognition service.")
        except Exception as e:
            speak("An error occurred.")
            print(e)
        return None

def get_gemini_response(message):
    data = {"contents": [{"role": "user", "parts": [{"text": message}]}]}  # Ensure this structure is correct

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={key}"
    response = requests.post(url, json=data)
    response.raise_for_status()  # This throws an error if the status code is not 200 OK

    response_json = response.json()
    response_text = response_json.get("candidates")[0].get("content").get("parts")[0].get("text")
    return response_text

if __name__ == "__main__":

    speak("Hello, I am your AI assistant. How can I assist you today?")
    while True:
        query = recognize_speech()
        if query:
            print(f"You said: {query}")
            if "exit" in query.lower() or "quit" in query.lower():
                speak("Goodbye!")
                break

            response = get_gemini_response(query)
            if response:
                print(f"Assistant: {response}")
                speak(response)