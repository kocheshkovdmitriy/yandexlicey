from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<string:title>')
@app.route('/index/<string:title>')
def main_page(title):
    return render_template('base.html', title=title)

@app.route('/training/<prof>')
def training(prof):
    return render_template('prof.html', prof=prof)

@app.route('/auto_answer /<a>/<b>')
def auto_answer(a, b):
    return render_template('prof.html', prof=prof)

if __name__ == "__main__":
    app.run(port=8000, host='127.0.0.1')