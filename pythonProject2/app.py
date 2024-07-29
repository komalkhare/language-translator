from flask import Flask, render_template, request
from googletrans import Translator, LANGUAGES

app = Flask(__name__)

# Create a dictionary of language codes and names
languages = {code: name.capitalize() for code, name in LANGUAGES.items()}


@app.route('/', methods=['GET', 'POST'])
def translate():
    translated_text = ""
    original_text = ""
    source_lang = "auto"
    target_lang = "en"

    if request.method == 'POST':
        original_text = request.form['text']
        source_lang = request.form['source_lang']
        target_lang = request.form['target_lang']

        translator = Translator()
        translation = translator.translate(original_text, src=source_lang, dest=target_lang)
        translated_text = translation.text

    return render_template('index.html',
                           original_text=original_text,
                           translated_text=translated_text,
                           source_lang=source_lang,
                           target_lang=target_lang,
                           languages=languages)


if __name__ == '__main__':
    app.run(debug=True)