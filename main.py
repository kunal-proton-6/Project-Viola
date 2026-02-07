import speech_recognition as sr
import webbrowser
import pyttsx3
import sys
import musicLibrary

def speak(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Speed of speech
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print(f"Error in speak: {e}")
        sys.stdout.flush()

def process_command(c):
    c = c.lower()
    print("Processing command: " + c)
    
    if "open google" in c:
        speak("Opening Google...")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c:
        speak("Opening Youtube...")
        webbrowser.open("https://www.youtube.com/@LotusOutlook")
    elif "open github" in c:
        speak("Opening GitHub...")
        webbrowser.open("https://github.com/lotus-outlook-6")
    elif "what is the time" in c or "tell me the time" in c:
        from datetime import datetime
        time = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")
    elif "what is your name" in c or "who are you" in c:
        speak("I am Viola, your AI assistant")
    elif "play" in c:
        # Extract song name from command (e.g., "play virtual" -> "virtual")
        # Remove "play" from start and handle "the" as a word, not substring
        song_name = c.replace("play", "", 1).strip()  # Remove first occurrence of "play"
        
        # Remove "the" if it's at the beginning as a separate word
        if song_name.startswith("the "):
            song_name = song_name[4:].strip()
        
        if song_name:
            link = musicLibrary.get_music_link(song_name)
            if link:
                speak(f"Playing {song_name}")
                webbrowser.open(link)
            else:
                available_songs = ", ".join(musicLibrary.list_available_songs())
                speak(f"Sorry, I don't have {song_name} in my library. Available songs are: {available_songs}")
        else:
            available_songs = ", ".join(musicLibrary.list_available_songs())
            speak(f"Available songs are: {available_songs}")
    else:
        speak("I didn't understand that command")
    

if __name__ == "__main__":
    print("Starting Viola...")
    try:
        speak("Initializing Viola...")
    except Exception as e:
        print(f"Warning: Initial speak failed - {e}")
        print("Continuing anyway...")
    
    while True:
        r = sr.Recognizer()
        
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                print("Listening...")
                try:
                    audio = r.listen(source, timeout=2, phrase_time_limit=2)
                except sr.WaitTimeoutError:
                    print("No speech detected, retrying...")
                    continue
                
                print("Recognizing...")
                try:
                    word = r.recognize_google(audio)
                    print(f"Heard: {word}")
                except sr.UnknownValueError:
                    print("Could not understand, retrying...")
                    continue
                
                # Check for stop listening command
                if "stop listening" in word.lower():
                    print("Stop listening command detected, exiting...")
                    speak("Stopping Viola. Goodbye!")
                    break
                
                if "viola" in word.lower():
                    print("Wake word detected!")
                    speak("Yes, how can I help you?")
                    print("Viola is listening for a command...")
                    try:
                        audio = r.listen(source, timeout=10, phrase_time_limit=10)
                    except sr.WaitTimeoutError:
                        print("Timed out, returning to listen mode...")
                        continue
                    
                    print("Recognizing...")
                    try:
                        command = r.recognize_google(audio)
                        print(f"Command received: {command}")
                        process_command(command)
                    except sr.UnknownValueError:
                        speak("I didn't understand that command")
        except sr.WaitTimeoutError:
            pass
        except Exception as e:
            print("Error!!! {0}".format(e))
            import traceback
            traceback.print_exc()