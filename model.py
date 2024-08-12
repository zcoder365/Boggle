import random

dice = [
    ['A', 'A', 'E', 'E', 'G', 'N'],
    ['E', 'L', 'R', 'T', 'T', 'Y'],
    ['A', 'O', 'O', 'T', 'T', 'W'],
    ['A', 'B', 'B', 'J', 'O', 'O'],
    ['E', 'H', 'R', 'T', 'V', 'W'],
    ['C', 'I', 'M', 'O', 'T', 'U'],
    ['D', 'I', 'S', 'T', 'T', 'Y'],
    ['E', 'I', 'O', 'S', 'S', 'T'],
    ['D', 'E', 'L', 'R', 'V', 'Y'],
    ['A', 'C', 'H', 'O', 'P', 'S'],
    ['H', 'I', 'M', 'N', 'Q', 'U'],
    ['E', 'E', 'I', 'N', 'S', 'U'],
    ['E', 'E', 'G', 'H', 'N', 'W'],
    ['A', 'F', 'F', 'K', 'P', 'S'],
    ['H', 'L', 'N', 'N', 'R', 'Z'],
    ['D', 'E', 'I', 'L', 'R', 'X'],
    ['A', 'I', 'L', 'M', 'R', 'S'],
    ['E', 'N', 'S', 'T', 'U', 'W'],
    ['A', 'E', 'G', 'M', 'N', 'N'],
    ['C', 'E', 'I', 'P', 'S', 'T'],
    ['A', 'D', 'E', 'N', 'N', 'N'],
    ['P', 'R', 'S', 'T', 'V', 'W'],
    ['E', 'I', 'I', 'I', 'T', 'T'],
    ['T', 'T', 'T', 'T', 'Y', 'Y'],
    ['G', 'O', 'R', 'R', 'V', 'W']
]

def getRandomLetters():
    # get random letters from each of the dice and store in a list
    letters = []
    
    for i in range(len(dice)):
        letter = random.choice(dice[i])
        letters.apppend(letter)
    
    return letters

def shuffleDice(dice):
    # shuffle the list of the dice so they're moved around
    shuffled = random.shuffle(dice)
    
    return shuffled