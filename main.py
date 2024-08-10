from flask import Flask, render_template, jsonify
from model import *
import time

# store the start time
start_time = None

app = Flask(__name__)

@app.route("/")
def home():
    letters = list(generateLetters())
    
    one = letters[0]
    two = letters[1]
    three = letters[2]
    four = letters[3]
    five = letters[4]
    six = letters[5]
    seven = letters[6]
    eight = letters[7]
    nine = letters[8]
    ten = letters[9]
    eleven = letters[10]
    twelve = letters[11]
    thirteen = letters[12]
    fourteen = letters[13]
    fifteen = letters[14]
    sixteen = letters[15]
    seventeen = letters[16]
    eighteen = letters[17]
    nineteen = letters[18]
    twenty = letters[19]
    twentyOne = letters[20]
    twentyTwo = letters[21]
    twentyThree = letters[22]
    twentyFour = letters[23]
    twentyFive = letters[24]
    
    return render_template("index.html", letter1=one, letter2=two, letter3=three, letter4=four, letter5=five, letter6=six, letter7=seven, letter8=eight, letter9=nine, letter10=ten, letter11=eleven, letter12=twelve, letter13=thirteen, letter14=fourteen, letter15=fifteen, letter16=sixteen, letter17=seventeen, letter18=eighteen, letter19=nineteen, letter20=twenty, letter21=twentyOne, letter22=twentyTwo, letter23=twentyThree, letter24=twentyFour, letter25=twentyFive)

@app.route('/get_time')
def get_time():
    global start_time
    
    if start_time is None:
        start_time = time.time()
    
    time_elapsed = int(time.time() - start_time)
    
    time_remaining = max(0, 180 - time_elapsed)
    
    while time_elapsed <= 180:
        print(f"Time Elapsed: {time_elapsed}\nTime Remaining: {time_remaining}")
        
        return jsonify({'time': time_remaining})

app.run(debug=True)