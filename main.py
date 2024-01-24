from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask!, we are live'

@app.route('/dota')
def hello_dota():
    return 'this is the dota route'

if __name__ == '__main__':
    app.run(debug=True)
