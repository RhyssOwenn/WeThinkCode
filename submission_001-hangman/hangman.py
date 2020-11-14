#TIP: use random.randint to get a random word from the list
#comment added
import random


def read_file(file_name):
   
    word_file = open(file_name,'r')
    text = word_file.readlines()
    word_file.close()
    
    return text


def select_random_word(words):
    
    randnum = random.randint(0,len(words) - 1)
    string = words[randnum].rstrip()
    letter = random.randint(0, len(string) - 1)
    print("Guess the word: " + string[:letter] + "_" + string[letter + 1:len(string)])
    return words[randnum]
    


def get_user_input():

    answer = input('\nGuess the missing letter: ')

    return answer


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

