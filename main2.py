from flask import Flask, request, current_app, make_response, redirect, render_template


app = Flask(__name__)



@app.route('/')
def requestdata():
    #return render_template('home.html')
    return "Hello! Your IP is {} and you are using {}: ".format(request.remote_addr,request.user_agent)

@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id)

@app.route('/books/<genre>/')
def books(genre):
    # return "All Books in {} category".format(genre)
    res = make_response("All Books in {} category".format(genre))
    res.headers['Content-Type'] = 'text/plain'
    res.headers['Server'] = 'Foobar'
    return res

@app.route('/set-cookie')
def set_cookie():
    res = make_response("Cookie setter")
    res.set_cookie("favorite-color", "skyblue")
    res.set_cookie("favorite-font", "sans-serif")
    return res

@app.route('/transfer')
def transfer():
    # return "", 302, {'location': 'https://localhost:5000/login'}
    return redirect("https://localhost:5000/login/")  

@app.route('/login/')
def login():
    # return "", 302, {'location': 'https://localhost:5000/login'}
    return "<h1>  You are on page LOGIN </h2>"     


if __name__ == "__main__":
    app.run(debug=True)
