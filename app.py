from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        return username

    else:
        return "methods error"

@app.route('/login')
def login():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
