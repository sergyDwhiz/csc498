# Language Translator

This project is a simple language translator web application built with Flask and googletrans. It uses a predefined Google Translate API to translate English text into various languages in real time without refreshing the page.

## Features

- **Real-Time Translation:** As you type in the source text, the app sends AJAX requests to translate the text instantly.
- **Language Selection:** Choose the target language from a dropdown.
- **Copy Translation:** Easily copy the translated text with a copy button.
- **Responsive Design:** The UI is built with Bootstrap and is responsive on mobile, tablet and desktop.
- **Custom Styling:** Uses the Ubuntu font from Google Fonts, with a clean, modern interface.

## Project Structure

```
/Users/sergiusnyah/csc498/
├── requirements.txt
├── run.py
├── README.md
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── language_translator.py
├── templates/
│   └── index.html
└── static/
    └── favicon.ico
```

- **requirements.txt** - Contains dependency list.
- **run.py** - Entry point for running the Flask application.
- **app/\*** - Contains the application package:
  - **__init__.py** - Initializes the Flask app and registers routes.
  - **routes.py** - Contains URL endpoint definitions, including the AJAX `/translate` route.
  - **language_translator.py** - Implements translation logic using googletrans.
- **templates/index.html** - The main HTML template.
- **static/favicon.ico** - The favicon for the project.

## How It Works

1. **Run the Application**
   Install the required packages (use `pip install -r requirements.txt`), then start the app with:
   ```
   python3 run.py
   ```
   The app will be served locally (typically at http://127.0.0.1:5000).

2. **Using the Translator**
   - Select the target language from the dropdown.
   - Enter the English text you want to translate.
   - The translation appears in real time on the right without needing to refresh the page.
   - Click the copy icon to copy the translation.

3. **Customization**
   The project is structured for easy expansion. You can add more routes, update styles in the CSS sections within the template, or modify translation logic in `language_translator.py`.

## Contributing

Feel free to fork the repository and submit pull requests. For any issues or suggestions, please open an issue on the GitHub repository.

---

Happy Translating!