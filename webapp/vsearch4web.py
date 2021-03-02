from flask import Flask, render_template, request, escape
from utils.vsearch import search4letters

app = Flask(__name__)


def log_request(req: "flask_requesrt", res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(str(dir(req)), res, file=log)


@app.route('/vsearch4', methods=['POST'])
def do_search() -> 'html':
    """Функция принимает данные отправленные через веб-форму и возвращает результат: request.form['phrase'] - фраза в
    которой будем искать нужные символы, request.form['letters'] - нужные символы."""
    title = 'Here are your results:'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html', the_title=title, the_phrase=phrase, the_letters=letters,
                           the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letter on the web!')


@app.route('/viewlog')
def view_the_log() -> str:
    with open("vsearch.log") as log:
        contents = escape(log.read())
    return contents


if __name__ == '__main__':
    app.run(debug=True)
