from flask import render_template, request, jsonify
from app import app
from app.language_translator import translate, LANGUAGES

@app.route('/', methods=['GET', 'POST'])
def index():
    translation = None
    lang_choice = None
    if request.method == 'POST':
        text = request.form.get('text', '')
        lang_choice = request.form.get('language', '').lower()
        if lang_choice in LANGUAGES:
            translation = translate(text, lang_choice)
    return render_template("index.html", translation=translation, languages=LANGUAGES, lang_choice=lang_choice)

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json() or {}
    text = data.get('text', '')
    lang = data.get('language', '').lower()
    if lang not in LANGUAGES:
        return jsonify({'error': 'Language not supported'}), 400
    result = translate(text, lang)
    return jsonify({'translation': result})
