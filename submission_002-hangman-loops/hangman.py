import random
import sys
from random import randint

##reads file returns text
def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()

#gets user guess 
def get_user_input():
    return input('Guess the missing letter: ')

#asks for text file
def ask_file_name():
    if len(sys.argv) > 1 and len(sys.argv) < 3:
        words_file = str(sys.argv[1])
        return words_file
    else:
        return "short_words.txt"

#selects random word
def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    print(word)
    return word


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    random_num= random.randint(0, len(word) - 1)
    letter = word[random_num]
    hiddenword = ""
    for i in range(len(word)):
        if i == random_num:
            hiddenword = hiddenword + letter
        else:
            hiddenword = hiddenword + "_"
    return hiddenword



# TODO: Step 1 - update to check if character is one of the missing characters
#compare input with chosen word, index through string function
def is_missing_char(original_word, answer_word, char):
    
    for i in range(len(original_word)):
        if original_word[i] == char and answer_word[i] == "_":
            return True
    return False


# TODO: Step 1 - fill in missing char in word and return new more complete word
# 
def fill_in_char(original_word, answer_word, char):
    newword = ""
    for i in range(len(original_word)):
        if original_word[i] == char and answer_word[i] == "_":
            newword += char
        else:
            newword += answer_word[i]
    return newword


def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer
    



# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    print('Wrong! Number of guesses left: '+str(number_guesses))
    draw_figure(number_guesses)


# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    if number_guesses == 4:
        print("""/----
|
|
|
|
_______""")
    elif number_guesses == 3:
        print("""/----
|   0
|
|
|
_______""")
    elif number_guesses == 2:
        print("""/----
|   0
|  /|\\
|   
|  
_______""")
    elif number_guesses == 1:
        print("""/----
|   0
|  /|\\
|   |
|
_______""")
    elif number_guesses == 0:
        print("""/----
|   0
|  /|\\
|   |
|  / \\
_______
""")



        


# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):
    guessnum = 5
    print("Guess the word: "+answer)
    while word != answer:
        
        guess = get_user_input()
        if guess == "exit" or guess == "quit":
            print("Bye!")
            break
        if is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess)
        else:
            guessnum -= 1
            do_wrong_answer(answer, guessnum)
            if guessnum == 0:
                print("Sorry, you are out of guesses. The word was:", word)
                break


# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":

    words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)
    run_game_loop(selected_word, current_answer)

