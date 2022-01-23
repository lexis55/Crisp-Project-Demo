from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'What do you think about to this Demo, Please comment TY!!!'

