
def create_outline():
    #creating a set
    topics = {"Introduction to Python", "Tools of the Trade", "How to make decisions", "How to repeat code ", "How to structure data", "Functions", "Modules"}
    #creating a list
    problems = ["Problem 1", "Problem 2", "Problem 3"]
    #creating multiple tuples in a list
    students = [("Nyari", "Introduction to Python", "Problem 2", "[STARTED]"), ("Adam", "How to make decisions", "Problem 1", "[GRADED]"), ("Jeff", "How to structure data", "Problem 3", "[STARTED]"),("Alice", "How to repeat code", "Problem 3", "[COMPLETED]")]
    #creating an empty dictionary
    dictionary = {}
    #creating a new list of topics
    topicslist = ["* Introduction to Python", "* Tools of the Trade", "* How to make decisions", "* How to repeat code", "* How to structure data", "* Functions", "* Modules"]
    #sorting the topics in alphabetic order
    topiclistsort = topicslist.sort()

    #iterating assigning problems "items" to topic key 
    for topic in topicslist:
        dictionary[topic] = problems

    #prints out sorted items of topicslist
    print("Course Topics:")
    for topic in topicslist:
        #format funtion
        print(f"{topic}")

    #prints out the key and items of the now filled dictionary, printing list as a string with the join function
    print("Problems:")
    for topic,value in dictionary.items():
        print(f"{topic} : {', '.join(value)}")

    #Orders from started to completed and num is the index number
    print("Student Progress: ")
    num = 1
    for student in (students):
        if student[3] == "[STARTED]":
            print(f"{num}. {', '.join(student)}")
            num+=1

    for student in (students):
        if student[3] == "[GRADED]":
            print(f"{num}. {', '.join(student)}")
            num+=1

    for student in (students):
        if student[3] == "[COMPLETED]":
            print(f"{num}. {', '.join(student)}")

if __name__ == "__main__":
    create_outline()