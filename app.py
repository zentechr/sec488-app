from flask import Flask, render_template, redirect, url_for, request, session
import time
import os

app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect('./login')
    else:
        OUTPUT = os.popen("cat " + session['filename']).read()
        return OUTPUT.replace('\n','<br>')

# Route for about.html
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'].lower() != 'morty':
            error = 'Invalid Credentials. Please try again.'
        else:
            if request.form['password'] == 'smith':
                session['logged_in'] = True
                session['filename'] = request.form['filename']
                return redirect('./')
            else:
                error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=False)
