from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('form.html')

@app.route('/Cafe/<name>')

def welcome(name):
    return f'welcome {name}'


@app.route('/login', methods = ['POST', 'GET'])

def login():
    if request.method=='POST':
        user= request.form['nm']
        return redirect(url_for('welcome', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('welcome', name=user))
if __name__ == '__main__':
    app.run(debug=True)