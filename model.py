import random

def generateLetters():
    letters = [] # keep track of letters generated
    
    for i in range(1, 26):
        letter = random.choice(alphabet)
        count[letter.lower()] += 1
        letters.append(letter)
        
    checkLetterCount(letters)
        
    return letters

def checkLetterCount(letters: list):
    for letter in letters:
        
        if count[letter.lower()] <= FINAL_COUNT[letter.lower()]:
            pass
        
        elif count[letter.lower()] > FINAL_COUNT[letter.lower()]:
            index = letters.index(letter)
            
            print(f"{letter} at index {index} exceeds letter count.")
            
            replaceLetter(letters, index)
            
            
def replaceLetter(letters_list: list, index: int):
    new_letter = random.choice(alphabet)
    letters_list[index] = new_letter
    count[new_letter.lower()] += 1
    
    print(f"{letters_list[index]} at index {index} replaced by {new_letter}.\n")