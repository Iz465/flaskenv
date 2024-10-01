from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/admin/<admin>')
def admin_page(admin):
    return f"{admin} as Admin"


@app.route('/guest')
def guest_page():
    return "Guest Page"

@app.route('/about')
def about_page():
    return "About Page"

@app.route('/contact')
def contact_page():
    return "Contact Page"


@app.route('/login/<name>')
def login_page(name):
    return f"Logged in as {name}"


@app.route('/user/<name>')

def hello_user(name):
    if name == 'admin':
        return redirect(url_for('admin_page', admin = name))
    else:
        return redirect(url_for('login_page', name = name))
    

if __name__ == ('__main__'):
    app.run(debug=True)