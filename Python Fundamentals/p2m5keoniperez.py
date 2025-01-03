import os 

os.system ("curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt")
elements = open('elements1_20.txt', 'r')
elementstxt = elements.read()
elmnt = elementstxt.split("\n")

def elements_quiz():

    name = input("Welcome, please provide your name: ")
    score = 0
    attempts = 5
    correctAns= []
    incorrectAns = []
    while True:
        userInp = input('Hi, enter an element name please: ')
        userInp = userInp.capitalize()
        while userInp in correctAns:
            if userInp in correctAns:
                print('No duplicates please! ')
                userInp = input('Enter an element name please: ')
                userInp = userInp.capitalize()
            if userInp not in correctAns:
                break
        if userInp in elmnt:
            score += 1
            print('Correct! ')
            correctAns.append(userInp)
        else:
            print('Incorrect! ')
            incorrectAns.append(userInp)
        attempts -=1 
        if attempts <= 0:
            break
    print(name.capitalize(), 'You\'ve scored:', score * 20, '% correct')
    print("Answers found:", correctAns)
    print("Incorrect answers:", incorrectAns)
    

elements_quiz()