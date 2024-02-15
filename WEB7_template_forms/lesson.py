from flask import Flask, request, render_template, redirect
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
@app.route('/')
def main_page():
    context = {
        'title': 'title page',
        'list': [1, 2, 3, 4, 5, 6]
    }
    return render_template('main_page.html', **context)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(request.form['username'])
        return redirect('/')
    return render_template('login.html', title='Авторизация', form=form)



if __name__ == "__main__":
    app.run(port=8000, host='127.0.0.1')
