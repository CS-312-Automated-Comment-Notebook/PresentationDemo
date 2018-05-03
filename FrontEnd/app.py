from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    subject = request.form['subject']
    processed_subject=subject.lower()
    processed_text = text.upper()
    processed_text1 = text.lower()
    return render_template("new.html",processed_text=processed_text,processed_text1=processed_text1,processed_subject=processed_subject)

if __name__ == '__main__':
    app.debug = True
    app.run()
