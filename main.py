import speech_recognition as sr
from gtts import gTTS
import os
from aws_services import AWSServices

# Initialize AWSServices instance
aws = AWSServices(region_name='us-east-1')

#gtts google voice 
language="en-UK"
text = "Hii,  i  am  Nex   your aws assistant How can i help you ?"
tts = gTTS(text=text, lang=language, slow=False)
tts.save("output.mp3")
os.system("afplay output.mp3")

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return ""



# Main function
def main():
    while True:
        command = recognize_speech()
       
        
        if command == "create instance":
            aws.create_ec2_instance()
        elif command == "stop instance":
            aws.stop_ec2_instance()
        elif command == "list instances":
            aws.list_ec2_instances()
        elif command == "exit":
            print("Exiting the voice assistant.")
            text = "ok bye"
            tts = gTTS(text=text, lang=language, slow=False)
            tts.save("output.mp3")
            os.system("afplay output.mp3")
            break
        else:
            print("Command not recognized. Please try again.")
if __name__ == "__main__":
    main()
