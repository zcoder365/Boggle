from flask import Flask, render_template, jsonify
from model import *
import time

# store the start time
start_time = None

app = Flask(__name__)

@app.route("/")
def home():
    letters = list(generateLetters())
    
    return render_template("index.html", letters=letters)

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