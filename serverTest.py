from flask import Flask, render_template, request, jsonify, redirect, url_for

import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('test.html')
    # return render_template('home.html', selection=request.form['rad'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)