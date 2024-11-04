from translate import Translator
from flask import Flask, render_template, request

app = Flask(__name__)

def translation(from_lang, to_lang, text):
    translator = Translator(from_lang=from_lang, to_lang=to_lang)
    return translator.translate(text)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/translate', methods=["GET", 'POST'])
def translate():
    if request.method == "POST":
        inputlanguage = request.form.get('sourceLanguage')
        targetlanguage = request.form.get('targetLanguage')
        text = request.form.get('texttoTranslate')
        translated_text = translation(inputlanguage, targetlanguage, text)
        return render_template('home.html', translated_text=translated_text)
    return render_template('home.html')

app.run(port=3000, debug=True)
