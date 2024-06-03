import speech_recognition as sr

# Create a Recognizer instance
recognizer = sr.Recognizer()

# Capture audio from microphone
with sr.Microphone() as source:
    print("Speak something...")
    audio = recognizer.listen(source)

# Recognize speech
try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, could not understand audio.")
except sr.RequestError as e:
    print("Error:", e)
