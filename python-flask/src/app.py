from flask import Flask
app = Flask(__name__)

@app.route('/test')
def hello_world():
    return 'hello world from /test path...'

def sample_function(str, num):
    return "!!!"
