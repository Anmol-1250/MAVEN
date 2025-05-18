from voice_recognition import listen_command
from navigation import follow_path
from tts import speak

def main():
    speak("Hello! I am your campus navigation assistant.")
    
    while True:
        command = listen_command()
        if "start navigation" in command:
            speak("Starting path navigation.")
            follow_path()
        elif "stop" in command:
            speak("Stopping. Goodbye!")
            break
        else:
            speak("Sorry, I didn't catch that. Please say a valid command.")

if __name__ == "__main__":
    main()
