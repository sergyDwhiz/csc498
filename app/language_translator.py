from googletrans import Translator, LANGUAGES  # new import

translator = Translator()  # new global instance

def translate(text, dest_language_code):  # changed code
    translation = translator.translate(text, dest=dest_language_code)
    return translation.text

def main():
    print("Simple English Translator using Google Translate")
    print("Available languages (code: language):")
    for code, name in LANGUAGES.items():
        print(f"{code}: {name}")

    lang_choice = input("Enter the target language code: ").strip().lower()
    if lang_choice not in LANGUAGES:
        print(f"Language code '{lang_choice}' not available.")
        return

    text = input("Enter text in English: ")
    result = translate(text, lang_choice)
    print(f"Translation into {LANGUAGES[lang_choice]}:", result)

if __name__ == '__main__':
    main()