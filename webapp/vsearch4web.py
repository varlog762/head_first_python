from flask import Flask, render_template, request, redirect
from utils.vsearch import search4letters

app = Flask(__name__)


@app.route('/')
def hello() -> '302':
    return redirect('/entry')


@app.route('/vsearch4', methods=['POST'])
def do_search() -> 'html':
    """Функция принимает данные отправленные через веб-форму и возвращает результат: request.form['phrase'] - фраза в
    которой будем искать нужные символы, request.form['letters'] - нужные символы."""
    title = 'Here are your results:'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    return render_template('results.html', the_title=title, the_phrase=phrase, the_letters=letters,
                           the_results=results)


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letter on the web!')


app.run(debug=True)
