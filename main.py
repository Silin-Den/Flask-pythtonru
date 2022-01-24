# %load main.py
from flask import Flask, render_template, make_response, current_app
from flask import url_for, request, redirect, flash
from flask_script import Manager, Command, Shell
from forms import ContactForm

app = Flask(__name__)
manager = Manager(app)

app.debug = True
app.config['SECRET_KEY'] = 'a really really really really long secret key'
# app.config['WTF_CSRF_ENABLED'] = False

@app.route('/')
def index():
    name, age, profession = "Jerry", 24, 'Programmer'
    template_context = dict(name=name, age=age, profession=profession)
    return render_template('index.html', **template_context)


@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return "Profile page of user # {}".format(user_id)


@app.route('/books/<genre>/')
def books(genre):
    # return "All Books in {} category".format(genre)
    res = make_response("All Books in {} category".format(genre))
    res.headers['Content-Type'] = 'text/plain'
    res.headers['Server'] = 'Foobar'
    return res

@app.route('/login/', methods=['post', 'get'])

def login():
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')  # запрос к данным формы
        password = request.form.get('password')


    if username == 'root' and password == 'pass':
        message = "Correct username and password"
    else:
        message = "Wrong username or password"

    return render_template('login.html', message=message)

@app.route('/contact/', methods=['get', 'post'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        print(name)
        print(email)
        print(message)
	# здесь логика базы данных
        print("\nData received. Now redirecting ...")
        flash("Message Received", "success")
        return redirect(url_for('contact'))

    return render_template('contact.html', form=form)

@app.route('/cookie/')
def cookie():
    if not request.cookies.get('foo'):
        res = make_response("Setting a cookie")
        res.set_cookie('foo', 'bar', max_age=60*60*24*365*2)
    else:
        res = make_response("Value of cookie foo is {}".format(request.cookies.get('foo')))
    return res

@app.route('/delete-cookie/')
def delete_cookie():
    res = make_response("Cookie Removed")
    res.set_cookie('foo', 'bar', max_age=0)
    return res

@app.route('/article/', methods=['POST',  'GET'])
def article():
    if request.method == 'POST':
        print(request.form)
        res = make_response("")
        res.set_cookie("font", request.form.get('font'), 60*60*24*15)
        res.headers['location'] = url_for('article')
        return res, 302

    return render_template('article.html')   

# class Faker(Command):
#     'Команда для добавления поддельных данных в таблицы'
#     def run(self):
#         # логика функции
#         print("Fake data entered")

# manager.add_command("faker", Faker())


# @manager.command
# def foo():
#     "Это созданная команда"
#     print("foo command executed")



# def shell_context():
#     import os, sys
#     return dict(app=app, os=os, sys=sys)

# manager.add_command("shell", Shell(make_context=shell_context))


if __name__ == "__main__":
    app.run()
    manager.run()


