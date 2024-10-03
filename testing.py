from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return redirect(url_for('hello_world'))

@app.route('/tests')
def hello_world():
    return render_template("welcome.html")

if __name__ == '__main__':
    app.run(debug=True)


