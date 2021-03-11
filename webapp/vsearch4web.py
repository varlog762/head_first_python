from flask import Flask, render_template, request, session
from webapp.utils.vsearch import search4letters
from DBcm import UseDataBase
from utils.checker import check_logged_in

app = Flask(__name__)
app.secret_key = 'UYGswyuGU*75^'

"""Flask.config - встроенный в Flask словарь для конфигурирования веб-приложения."""
app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': 'vsearchpasswd',
                          'database': 'vsearchlogDB', }


def log_request(req: "flask_requesrt", res: str) -> None:
    """Журналирует веб-запрос и возвращаемые результаты."""
    with UseDataBase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log (phrase, letters, ip, browser_string, results) values (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.browser,
                              res,))


@app.route('/vsearch4', methods=['POST'])
def do_search() -> 'html':
    """Функция принимает данные отправленные через веб-форму и возвращает результат: request.form['phrase'] - фраза в
    которой будем искать нужные символы, request.form['letters'] - нужные символы."""
    title = 'Here are your results:'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    try:
        log_request(request, results)
    except Exception as err:
        print(f"***** Что-то пошло не так: {err}")
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letter on the web!')


@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    with UseDataBase(app.config['dbconfig']) as cursor:
        _SQL = '''select phrase, letters, ip, browser_string, results from log'''
        cursor.execute(_SQL)
        contents = cursor.fetchall()

    titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results',)
    return render_template('viewlog.html',
                           the_title='View log',
                           the_row_titles=titles,
                           the_data=contents,)


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in!'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out'


if __name__ == '__main__':
    app.run(debug=True)
