from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Welcome to my app"

@app.route('/sayhi/<name>', methods=['GET', ])
def sayhi(name):
    return "Say hi, " + name

@app.route('/sayhi2/<name>', methods=['GET', ])
def sayhi2(name):
    return "Say hi, " + name

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)