from gasp import *
from random import randint
from gasp.utils import read_yesorno

def set_var():
    answer = randint(1, 1000)
    guesses = 0
    question = """OK, I've thought of a number between 1 and 1000. 
    """
    guessing = "Make a guess: "

def asking():
    answer = randint(1, 1000)
    guesses = 0
    question = """OK, I've thought of a number between 1 and 1000. 
    """
    guessing = "Make a guess: "
    print(question)
    while True:
        guess = int(input(guessing))
        if answer - guess > 0:
            guesses += 1
            print("""That's too low.
            """)
        elif answer - guess < 0:
            guesses += 1
            print("""That's too high.
            """)
        elif answer - guess == 0:
            print(f"That was my number. Well done!\n\nYou took {guesses} guesses.")
            play_again = input("Would you like another game? ") # Had a problem with read_yesorno. It would keep saying "Please answer yes or no." even though I was answering "yes" and "no" 
            if play_again == "yes":
                answer = randint(1, 1000)
                guesses = 0
                print(f"\n\n{question}")
            elif play_again == "no":
                break
asking()

