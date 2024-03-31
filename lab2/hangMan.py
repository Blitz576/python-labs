import random

# Define The List Of Words
WORDS = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange']

# Randomly Selecting A word
word = list(random.choice(WORDS))
guess = []

# fill guess with _
for letter in word:
    guess.append("_")


# Function To Manipulate The guess word
def manibulate(letter):
    matched = 0
    for i in range(len(word)):
        if letter == word[i]:
            guess[i] = letter
            matched += 1
    return matched




# Define Number Of chances
tries = 7

#Test Cases Loop
for trie in range(tries) :
    letter = input('Guess a letter: ')
    matches = manibulate(letter)
    print(f'You have {matches}')
    print(f'your string is {"".join(guess)}')
    print(f'You have {tries-(trie+1)} tries left')
    if word == guess:
        print('Congratulations! You Won')
        break
else:
   print('Sorry you did not guess the word')