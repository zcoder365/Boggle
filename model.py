from ascii import ascii_uppercase # type: ignore
import random

# letter occurrances in the boggle square
COUNT = {
    "a": 12,
    "b": 1,
    "c": 5,
    "d": 6,
    "e": 19,
    "f": 4,
    "g": 3,
    "h": 5,
    "i": 11,
    "j": 1,
    "k": 1,
    "l": 5,
    "m": 4,
    "n": 11,
    "o": 11,
    "p": 4,
    "q": 1,
    "r": 12,
    "s": 9,
    "t": 13,
    "u": 4,
    "v": 1,
    "w": 12,
    "x": 1,
    "y": 3,
    "z": 1,
}

# generate list of letters
alphabet = list(ascii_uppercase())
count = {
        "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
    }

def generate_letters():
    letters = [] # keep track of letters generated
    
    for i in range(25):
        letter = random.choice(alphabet)
        updateLetterCount(letter)

def updateLetterCount(letter):
        if letter == "A":
            count["a"] += 1
        if letter == "B":
            count["b"] += 1
        if letter == "C":
            count["c"] += 1
        if letter == "D":
            count["d"] += 1
        if letter == "E":
            count["e"] += 1
        if letter == "F":
            count["f"] += 1
        if letter == "G":
            count["g"] += 1
        if letter == "H":
            count["h"] += 1
        if letter == "I":
            count["i"] += 1
        if letter == "J":
            count["j"] += 1
        if letter == "K":
            count["k"] += 1
        if letter == "L":
            count["l"] += 1
        if letter == "M":
            count["m"] += 1
        if letter == "N":
            count["n"] += 1
        if letter == "O":
            count["o"] += 1
        if letter == "P":
            count["p"] += 1
        if letter == "Q":
            count["q"] += 1
        if letter == "R":
            count["r"] += 1
        if letter == "S":
            count["s"] += 1
        if letter == "T":
            count["t"] += 1
        if letter == "U":
            count["u"] += 1
        if letter == "V":
            count["v"] += 1
        if letter == "W":
            count["w"] += 1
        if letter == "X":
            count["x"] += 1
        if letter == "Y":
            count["y"] += 1
        if letter == "Z":
            count["z"] += 1
            
def checkLetterCounts(letters_list):
    for letter in letters_list:
        if count[letter.lower()] <=