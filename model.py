import ascii
import random

# letter occurrances in the boggle square (final)
FINAL_COUNT = {
    "a": 12, "b": 1, "c": 5, "d": 6, "e": 19, "f": 4, "g": 3, "h": 5, "i": 11, "j": 1, "k": 1, "l": 5, "m": 4, "n": 11, "o": 11, "p": 4, "q": 1, "r": 12, "s": 9, "t": 13, "u": 4, "v": 1, "w": 12, "x": 1, "y": 3, "z": 1,
}

# generate list of letters
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# keep track of the count of the letters (changing)
count = {
    "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
}

def generateLetters():
    letters = [] # keep track of letters generated
    
    for i in range(25):
        letter = random.choice(alphabet)
        updateLetterCount(letter)
    
    checkLetterCounts(letters)
        
    return letters

def updateLetterCount(letter):
    count[letter.lower()] += 1
            
def checkLetterCounts(letters_list):
    for letter in letters_list:
        if count[letter.lower()] <= FINAL_COUNT[letter.lower()]:
            pass
        
        elif count[letter.lower()] > FINAL_COUNT[letter.lower()]:
            letter_to_change = letters_list.index(letter)
            
            new_letter = random.choice(alphabet)
            
            letters_list[letter_to_change] = new_letter