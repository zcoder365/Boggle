from flask import Flask, render_template
from model import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", letter1="X", letter2="X", letter3="X", letter4="X", letter5="X", letter6="X", letter7="X", letter8="X", letter9="X", letter10="X", letter11="X", letter12="X", letter13="X", letter14="X", letter15="X", letter16="X", letter17="X", letter18="X", letter19="X", letter20="X", letter21="X", letter22="X", letter23="X", letter24="X", letter25="X")

@app.route("/shuffle")
def shuffle():
    generate_letters()
    
    return render_template("index.html", letter1="X", letter2="X", letter3="X", letter4="X", letter5="X", letter6="X", letter7="X", letter8="X", letter9="X", letter10="X", letter11="X", letter12="X", letter13="X", letter14="X", letter15="X", letter16="X", letter17="X", letter18="X", letter19="X", letter20="X", letter21="X", letter22="X", letter23="X", letter24="X", letter25="X")

app.run(debug=True)