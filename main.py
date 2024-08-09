from flask import Flask, render_template
from model import *

app = Flask(__name__)

@app.route("/")
def home():
    letters = list(generateLetters())
    
    return render_template("index.html", letter1=letters[0], letter2=letters[1], letter3=letters[2], letter4=letters[3], letter5=letters[4], letter6=letters[5], letter7=letters[6], letter8=letters[7], letter9=letters[8], letter10=letters[9], letter11=letters[10], letter12=letters[11], letter13=letters[12], letter14=letters[13], letter15=letters[14], letter16=letters[15], letter17=letters[16], letter18=letters[17], letter19=letters[18], letter20=letters[19], letter21=letters[20], letter22=letters[21], letter23=letters[22], letter24=letters[23], letter25=letters[24])

app.run(debug=True)