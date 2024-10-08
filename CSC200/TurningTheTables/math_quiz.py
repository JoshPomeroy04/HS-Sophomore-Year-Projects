from gasp import *
from random import randint

correct = 0

def questions():
    global correct
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    question = "What's " + str(num1) + ' times ' + str(num2) + '? '
    answer = int(input(question))
    coranswer = num1*num2
    if answer == coranswer:
        print("That’s right – well done.")
        correct += 1
    else:
        print("No, I’m afraid the answer is " + str(coranswer) + '.')

def score():
    global correct
    print("I asked you 10 questions. You got " + str(correct) +  " of them right.")
    print("Well done!")

def main():
    for thing in range(10):
        questions()

    score()

main()
