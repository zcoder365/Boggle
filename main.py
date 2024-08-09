from flask import Flask, render_template
from model import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/shuffle")
def shuffle():
    chosen_letters = generateLetters()
    
    return render_template("index.html", letter1=chosen_letters[0], letter2=chosen_letters[1], letter3=chosen_letters[2], letter4=chosen_letters[3], letter5=chosen_letters[4], letter6=chosen_letters[5], letter7=chosen_letters[6], letter8=chosen_letters[7], letter9=chosen_letters[8], letter10=chosen_letters[9], letter11=chosen_letters[10], letter12=chosen_letters[11], letter13=chosen_letters[12], letter14=chosen_letters[13], letter15=chosen_letters[14], letter16=chosen_letters[15], letter17=chosen_letters[16], letter18=chosen_letters[17], letter19=chosen_letters[18], letter20=chosen_letters[19], letter21=chosen_letters[20], letter22=chosen_letters[21], letter23=chosen_letters[22], letter24=chosen_letters[23], letter25=chosen_letters[24])

app.run(debug=True)