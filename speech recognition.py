import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk  # Ensure pywhatkit is installed using `pip install pywhatkit`

# Initialize recognizer and text-to-speech engine
listening = sr.Recognizer()
engine = pt.init()

# Define the speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define the hear function
def hear():
    try:
        with sr.Microphone() as mic:
            print('Listening...')
            voice = listening.listen(mic)  # Listen to the user's voice
            cmd = listening.recognize_google(voice)  # Recognize the speech
            cmd = cmd.lower()  # Convert to lowercase for easier processing
            if 'mdtan' in cmd:  # Check if the keyword "kodi" is present
                cmd = cmd.replace('mdtan', '').strip()  # Remove "kodi" and strip whitespace
                print(f"Command after processing: {cmd}")
            return cmd  # Return the processed command
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, there seems to be an issue with the speech recognition service.")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

# Define the run function
def run():
    cmd = hear()  # Get the command
    if cmd:  # Proceed only if a command was received
        print(f"Command received: {cmd}")
        if 'play' in cmd:  # Check if the command contains "play"
            song = cmd.replace('play', '').strip()  # Extract the song name
            speak(f"Playing {song}")
            pk.playonyt(song)  # Play the song on YouTube using pywhatkit

# Run the program
run()
