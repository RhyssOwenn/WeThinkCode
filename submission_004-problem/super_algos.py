
def checkdigit(list):
    '''function checks if items of a list are integers'''

    for i in range(len(list)):
        if type(list[i]) != int:
            return False
        else:
            return True


def find_min(element):
    '''function finds the smallest number in a list'''
    if checkdigit(element) == False:
        return -1
    elif len(element) == 1:
        return element[0]
    elif len(element) == 0:
        return -1
    else:
        minDigit = find_min(element[1:])
        placeholder = element[0]
        if minDigit < placeholder:
            placeholder = minDigit
        return placeholder



def sum_all(element):
    '''function sums all integers in a list together'''

    if len(element) == 0:
        return -1
    elif checkdigit(element) == False:
        return -1
    elif len(element) == 1:
        return element[0]
    else:
        return element[0]+sum_all(element[1:]) 



def find_possible_strings(character_set, a):
    '''
    first part of permutation program, function checks that all items are characters and length of permutation as well as calls second function with empty list to iterate each character
    '''

    if a == 1:
        return character_set
    elif checkdigit(character_set) == True:
        return []
    n = len(character_set)
    emptylis = []
    result = find_possible_strings2(character_set, "", n, a, emptylis)
    return result
    

def find_possible_strings2(set, newstr, n, a, emptylis): 
    '''
    function iterates through each possible combination of characters
    '''

    if (a == 0) : 
        print(newstr)
        emptylis.append(newstr)
        return
    for i in range(n): 
        newPrefix = newstr + set[i] 
        find_possible_strings2(set, newPrefix, n, (a - 1), emptylis)
    return emptylis
        
        

numlist = [5, 9, 3, 5, 1, 8]
a = find_min(numlist)
print(a)
my_list = [4,6,3,8]

b = sum_all(my_list)
print(b)

letters = ['a', 'b']
times = 3
a = find_possible_strings(letters,times)
print(a)