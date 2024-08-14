from flask import Flask, render_template, jsonify
from model import *
import time

# store the start time
start_time = None

app = Flask(__name__)

@app.route("/")
def home():
    letters = getRandomLetters()
    shuffled_letters = shuffleDice(letters)
    
    return render_template("index.html", letter1=shuffled_letters[0], letter2=shuffled_letters[1], letter3=shuffled_letters[2], letter4=shuffled_letters[3], letter5=shuffled_letters[4], letter6=shuffled_letters[5], letter7=shuffled_letters[6], letter8=shuffled_letters[7], letter9=shuffled_letters[8], letter10=shuffled_letters[9], letter11=shuffled_letters[10], letter12=shuffled_letters[11], letter13=shuffled_letters[12], letter14=shuffled_letters[13], letter15=shuffled_letters[14], letter16=shuffled_letters[15], letter17=shuffled_letters[16], letter18=shuffled_letters[17], letter19=shuffled_letters[18],letter20=shuffled_letters[19], letter21=shuffled_letters[20], letter22=shuffled_letters[21], letter23=shuffled_letters[22], letter24=shuffled_letters[23], letter25=shuffled_letters[24])

# @app.route('/get_time')
# def get_time():
#     global start_time
    
#     if start_time is None:
#         start_time = time.time()
    
#     time_elapsed = int(time.time() - start_time)
    
#     time_remaining = max(0, 179 - time_elapsed)
    
#     while time_elapsed <= 179:
#         print(f"Time Elapsed: {time_elapsed}\nTime Remaining: {time_remaining}")
        
#         return jsonify({'time': time_remaining})

app.run(debug=True)