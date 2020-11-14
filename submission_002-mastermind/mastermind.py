
import random

##Checks whether input and code are the same and successful 
def report_results(correctposition, correctdigits, hiddencode, guess, listguess, turns):
    if correctposition == correctdigits:
        correctdigits = correctdigits - correctdigits

    print("Number of correct digits in correct place:    ",correctposition)
    print("Number of correct digits not in correct place:",correctdigits)

    if(hiddencode == listguess):
        print("Congratulations! You are a codebreaker!\nThe code was:",guess)
        return True
    else:
        print("Turns left:", turns)
    return False


#compares input and hiddencode to see how many are correct 
def check_digits(guess, hcode):
    index = 0
    correctdig = 0

    while index < 4:
        index2 = 0
        while(index2 < 4):
            if hcode[index] == guess[index2]:
                correctdig+=1
            index2+=1
        index+=1
    correcdig = len(hcode) - 1
    return correctdig



#compares input and hiddencode to see how many are in correct position
def check_position(guess, hcode):
    index = 0
    numberofcorrectdigits = 0

    while index < 4:
        if hcode[index] == guess[index]:
            numberofcorrectdigits += 1
        index+=1
    return numberofcorrectdigits

#gets user input
def get_user_input():
    guess = input("Input 4 digit code: ")
    while len(guess) != 4 or guess.isdigit() == False:
        print("Please enter exactly 4 digits.")
        guess = input("Input 4 digit code: ")
    return guess
    
#converts guess string of numbers to a list
def convert_to_list(guess):
    newguess = list(guess)
    for index in range(len(newguess)):
        newguess[index] = int(newguess[index])
    return(newguess)

#randomly assigns 4 integers to a list
def get_hidden_code():
    lis = []
    while len(lis) < 4:
            digit = random.randint(1,8)
            if digit not in lis:
                lis.append(digit)
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    return lis

#main game code, loops until guess is right or user runs out of turns
def run_game():
    turns = 12
    hidden_code = get_hidden_code()
    while True:
        guess = get_user_input()
        listguess = convert_to_list(guess)
        corrcpos = check_position(listguess, hidden_code)
        corrcdig = check_digits(listguess, hidden_code)
        turns -= 1
        finalresult = report_results(corrcpos, corrcdig, hidden_code, guess, listguess, turns)
        if turns == 0 or finalresult == True:
            break
        
        


if __name__ == "__main__":
    run_game()
