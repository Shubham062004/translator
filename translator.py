import io
import time
import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import pygame

# Supported regional languages mapping
LANGUAGES = {
    "1": ("English", "en", "en-US"),
    "2": ("Hindi", "hi", "hi-IN"),
    "3": ("Tamil", "ta", "ta-IN"),
    "4": ("Telugu", "te", "te-IN"),
    "5": ("Gujarati", "gu", "gu-IN")
}

def display_languages():
    print("\n--- Available Languages ---")
    for key, value in LANGUAGES.items():
        print(f"{key}. {value[0]}")

def get_language_choice(prompt):
    while True:
        display_languages()
        choice = input(prompt).strip()
        if choice in LANGUAGES:
            return LANGUAGES[choice]
        print("Invalid choice. Please select a valid number.")

def get_voice_input(sr_code):
    # This directly accesses your PC mic without saving any audio files
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nAdjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening... Speak directly into your mic now!")
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Processing voice input...")
            text = recognizer.recognize_google(audio, language=sr_code)
            print(f"Recognized Text: {text}")
            return text
        except sr.WaitTimeoutError:
            print("Listening timed out. No speech detected.")
            return None
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Connection error: {e}")
            return None

def main():
    # Initialize the pygame mixer for direct speaker access
    pygame.mixer.init()
    
    print("=== Python Regional Translator (No-File Version) ===")
    
    # 1. Select Input and Output Languages
    input_lang_name, input_trans_code, input_sr_code = get_language_choice("Select INPUT language (Enter number): ")
    output_lang_name, output_trans_code, _ = get_language_choice("Select OUTPUT language (Enter number): ")
    
    print(f"\nConfigured: Translating from {input_lang_name} to {output_lang_name}")
    
    # 2. Select Input Mode (Text or Voice)
    while True:
        mode = input("\nChoose input mode:\n1. Text Input\n2. Voice Input (Direct Mic)\nEnter 1 or 2: ").strip()
        if mode in ["1", "2"]:
            break
        print("Invalid choice. Please enter 1 or 2.")
        
    text_to_translate = ""
    
    if mode == "1":
        text_to_translate = input(f"\nEnter the text in {input_lang_name}: ").strip()
    else:
        text_to_translate = get_voice_input(input_sr_code)
        
    if not text_to_translate:
        print("No text found to translate. Exiting program.")
        return

    # 3. Translation Process
    print("\nTranslating...")
    try:
        translated_text = GoogleTranslator(source=input_trans_code, target=output_trans_code).translate(text_to_translate)
        print(f"\n--- Original ({input_lang_name}) ---")
        print(text_to_translate)
        print(f"\n--- Translated ({output_lang_name}) ---")
        print(translated_text)
        
        # 4. Stream Audio Directly to Speakers
        print("\nStreaming audio directly to speakers...")
        tts = gTTS(text=translated_text, lang=output_trans_code, slow=False)
        
        # Create an in-memory byte buffer instead of a physical file
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        
        # Reset the buffer's position to the beginning before playing
        audio_fp.seek(0)
        
        # Load the audio stream directly into pygame mixer
        pygame.mixer.music.load(audio_fp)
        pygame.mixer.music.play()
        
        # Keep the script running just long enough for the audio to finish
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
            
        print("Playback finished cleanly.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()