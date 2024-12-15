# Import the required modules for text-to-speech conversion
from gtts import gTTS
import os

# Function to convert text to speech
def text_to_speech():
    print("\n--- Text to Speech Converter ---")
    
    # Taking user input for the text to convert
    mytext = input("\nEnter the text you want to convert to speech: \n")
    if not mytext.strip():
        print("Error: No text entered. Please try again.")
        return
    
    # Taking user input for language
    language = input("\nEnter the language code (default is 'en' for English): ").strip() or 'en'

    # Choosing playback speed
    speed_choice = input("\nDo you want slow speech? (yes/no, default is 'no'): ").strip().lower()
    slow = True if speed_choice == 'yes' else False

    # Passing the text and language to the engine
    try:
        myobj = gTTS(text=mytext, lang=language, slow=slow)

        # Saving the converted audio in a mp3 file named output.mp3
        filename = "output.mp3"
        myobj.save(filename)
        print(f"\nAudio saved as {filename}")

        # Playing the converted file
        os.system(f"start {filename}")
    except Exception as e:
        print(f"\nError: {e}")

# Main program execution
if __name__ == "__main__":
    text_to_speech()
