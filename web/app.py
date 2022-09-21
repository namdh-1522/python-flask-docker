from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'Hello Flask. ENV Value = {os.getenv("TEST_ENV")}'

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')