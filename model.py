from ascii import ascii_uppercase # type: ignore
import random

# letter occurrances in the boggle square
A_COUNT = 12
B_COUNT = 1
C_COUNT = 5
D_COUNT = 6
E_COUNT = 19
F_COUNT = 4
G_COUNT = 3
H_COUNT = 5
I_COUNT = 11
J_COUNT = 1
K_COUNT = 1
L_COUNT = 5
M_COUNT = 4
N_COUNT = 11
O_COUNT = 11
P_COUNT = 4
Q_COUNT = 1
R_COUNT = 12
S_COUNT = 9
T_COUNT = 13
U_COUNT = 4
V_COUNT = 1
W_COUNT = 2
X_COUNT = 1
Y_COUNT = 3
Z_COUNT = 1

# generate list of letters
alphabet = list(ascii_uppercase())

def generate_letters():
    letters = [] # keep track of letters generated
    
    count = {
        "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
    }
    
    for i in range(25):
        letter = random.choice(alphabet)
        
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