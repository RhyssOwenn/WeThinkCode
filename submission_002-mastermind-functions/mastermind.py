import random


def get_hidden_code():
    '''
    creates an unkown code for user to guess at
    '''
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) ## 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    #print(code)
    return code


def get_user_input():
    '''
    takes in user input of 4 digits
    '''
    answer = input("Input 4 digit code: ")
    while len(answer) != 4 or answer.isdigit() == False:
        print("Please enter exactly 4 digits.")
        answer = input("Input 4 digit code: ")
    return answer


def checkdig(code, answer, turns):
    '''
    compares user guess with hidden code and prints number of correct guessed positions + numbers and number of correct numbers
    '''
    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
            if code[i] == int(answer[i]):
                correct_digits_and_position += 1
            elif int(answer[i]) in code:
                correct_digits_only += 1
    print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
    print('Number of correct digits not in correct place: '+str(correct_digits_only))
    if correct_digits_and_position == 4:
                correct = True
                print('Congratulations! You are a codebreaker!')
                return correct
    else:
        print('Turns left: '+str(11 - turns))
        correct = False
        return correct


def gameloop(code):
    '''
    loops through game until turns run out or user guesses correctly
    '''
    correct = False
    turns = 0
    while not correct and turns < 12:
        answer = get_user_input()
        correct = checkdig(code, answer, turns)
        turns += 1


def printresult(code):
    '''
    prints the result
    '''
    print('The code was: '+str(code))


# TODO: Decompose into functions
def run_game():
    code = get_hidden_code()
    gameloop(code)
    printresult(code)
    

if __name__ == "__main__":
    run_game()
