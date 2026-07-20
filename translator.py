"""
English -> Any Language Translator
------------------------------------
Uses the free `deep-translator` package (Google Translate backend).
No API key required.

Install dependency first:
    pip install deep-translator

Run:
    python translator.py
"""

import sys
from deep_translator import GoogleTranslator

# Ensure UTF-8 output encoding for Windows terminals
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# A few common language codes for reference.
# Full list: GoogleTranslator().get_supported_languages(as_dict=True)
COMMON_LANGUAGES = {
    "hindi": "hi",
    "punjabi": "pa",
    "spanish": "es",
    "french": "fr",
    "german": "de",
    "chinese": "zh-CN",
    "japanese": "ja",
    "arabic": "ar",
    "russian": "ru",
    "portuguese": "pt",
    "italian": "it",
    "korean": "ko",
    "urdu": "ur",
    "bengali": "bn",
    "tamil": "ta",
}


def translate_text(text: str, target_lang: str, source_lang: str = "en") -> str:
    """Translate text from source_lang to target_lang."""
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    return translator.translate(text)


def resolve_language_code(user_input: str) -> str:
    """Allow user to type either a language name (e.g. 'french') or a code (e.g. 'fr')."""
    key = user_input.strip().lower()
    return COMMON_LANGUAGES.get(key, key)  # fall back to raw input as a code


def main():
    print("=== English to Other Language Translator ===")
    print("Example languages:", ", ".join(COMMON_LANGUAGES.keys()))
    print("(You can also type an ISO code like 'fr', 'hi', 'es', etc.)")
    print("Type 'quit' at any time to exit.\n")

    while True:
        text = input("Enter English text to translate: ").strip()
        if text.lower() == "quit":
            break
        if not text:
            print("Please enter some text.\n")
            continue

        lang_input = input("Translate to which language? ").strip()
        if lang_input.lower() == "quit":
            break

        target_code = resolve_language_code(lang_input)

        try:
            result = translate_text(text, target_code)
            print(f"\nTranslated ({lang_input}): {result}")

            # Append to translations.txt file with UTF-8 encoding
            with open("translations.txt", "a", encoding="utf-8") as f:
                f.write(f"[{lang_input}] {text} -> {result}\n")
            print("-> Saved to translations.txt\n")

        except Exception as e:
            print(f"\nError: could not translate. Details: {e}\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting translator. Goodbye!")

