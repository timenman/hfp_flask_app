from flask import Flask, render_template, request
from search4letters import search4letters


app = Flask(__name__)

def log_request(req:'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req, res, file=log)

@app.route('/')
def hello() -> str:
    return 'Hello, World!'

@app.route('/entry')
def entry() -> 'html':
    return render_template('entry.html')

@app.route('/search4', methods=['POST'])
def search4() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                            the_title = title,
                            the_phrase = phrase,
                            the_letters = letters,
                            the_results = results)

@app.route('/viewlog')
def view_log() -> 'html':
    with open('vsearch.log', 'r') as log:
        contents = log.read()
    return render_template('view_log.html',
                            contents = contents)

if __name__ == '__main__' :
    app.run(debug=True)

