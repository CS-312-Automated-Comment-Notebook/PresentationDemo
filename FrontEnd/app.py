from flask import Flask
from flask import request
from flask import render_template
from evalast import comment
from autodocgen import autoDocGenerator
from autocomment import repComms


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['TEXTAR']
    text1 = request.form['TEXTAR1']
    type=text1
    with open ('user.py', "w") as f:
      f.write (text);
    commdic = comment(text)
    repComms('user.py',commdic) # autocommenting 
    autoDocGenerator('user.py', type) # autodocing and jupyter notebooks generation
    return render_template("new.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
