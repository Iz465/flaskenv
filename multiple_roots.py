from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/hello1/<name>')
def hello_world1(name):
    return f"Hello {name}"

@app.route('/hello2/<name>')
def hello_world2(name):
    return f"Hello {name}"

@app.route('/hello3/<name>')
def hello_world3(name):
    return f"Hello {name}"



if __name__ == '__main__':
    app.run(debug=True)