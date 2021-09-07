'''
Author: Jordan
Version: 1

1. Give a brief description of how the code below works.
   Use plain, accessible language and avoid repeating
   the exact statements from the code. Aim to write at
   least 3 sentences.
   
In this code, it works by asking some get to know you questions (name) to the player. Then, it gives directions to the
player and then gueesing commences. They must pick a number between 1 and 10. The game will spit back hints to the
player after each guess on if they are higher or lower than the correct input. Once the player answers correctly, they win!

2. Make a modification to the code in some place that changes the game
   in some interesting way. This cannot be as simple as changing the
   MINIMUM or one of the printed messages, but make enough changes and
   they can add up. You might allow the player to play more rounds after
   the first one, or completely change all the messages to have a pirate
   theme, or make it so the player can specify the maximum number.
   Describe your change here clearly and explain why you thought it was
   interesting.
   
I am first going to change the maximum input to 100. Why? Why not. Next, I am going to make it themed all around
how many pizzas Pizza Paul ate. Once they guess correctly, it will give them a slice of either cheese
or pepporoni pizza (just a picture). And, if they do not type in the proper number they have to restart.
This is part of the game. I thought making it into a pizza theme was interesting because it is easy to implement
and just a fun thing to work on at the end of the day. Also, I know it is easy to make pizza text drawings,
so that is why I went ahead and did so. And just for laughs, I changed the maximum number to 100 slices.
In the end, I think I made some good modifications. Lastly, I added some things we learned from lesson 12-15
like the triple quotes, escape characters, and print functions for extra added practice.

'''

# Import the randint function generate random integers
from random import randint

# Establish the lower and uppper bound on the goal number
MINIMUM = 1
MAXIMUM = 100

def print_welcome():
    '''
    Prompt the user for their name, and then display a
    simple message explaining the rules of the game.
    '''
    # Get the name of the user
    name = input("Welcome, What is your name? ")
    # Show the user's name
    print("Hello", name, "and welcome to Pizza Paul's guessing game!")
    # Print out the limits of the goal number
    print("I've eaten a number of slices between", MINIMUM, "and", MAXIMUM)
    # Write out rest of the instructions
    print("You'll need to guess how many to win a slice of pizza.")
    print("I'll tell you if I ate more or less.")
    
def print_ending():
    '''
    Print out a conclusive message to wrap up the game.
    '''
    print("You win!")
    
    inp = input("Now, pick a number 1 or 2 for a slice of cheese or pepporoni pizza on the house. It could be either!\n")
    if inp == "1":
        print("""_______________
\   o     o   /
 \ o         /
  \     o   /
   \ o     /
    \   o /
     \   /
      \o/
       V
                  
    """)
                        
    elif inp == "2":
        print("""_______________
\             /
 \           /
  \         /
   \       /
    \     /
     \   /
      \ /
       V
             
    """)
    
    else:
        print("Please only choose between 1 and 2. Since you did not follow instructions, you will have to retry for a chance at a slice of pizza.")
    
def process_guess(guess, goal):
    '''
    Print out whether or not the user was above, below,
    or at the goal.
    
    Args:
        guess (int): The number that the user entered
            as their guess.
        goal (int): The number that the computer is
            thinking of.
    '''
    # Branch execution based on whether the guess was right
    if guess < goal:
        print("Pizza Paul ate more!")
    elif guess > goal:
        print("Pizza Paul did not each that much!")
    else:
        print("That's correct, it's", goal, "slices of pizza.")

def get_number():
    '''
    Ask the user for a number, and keep prompting
    them until they give you an actual number
    (as opposed to giving you a letter).
    '''
    # Get the guess from the user, returns a string
    number = input("What is your guess? ")
    # Was the string composed only of numbers?
    if number.isdigit():
        # If so, we can safely convert it to an integer
        number_as_int = int(number)
        # And return the result
        return number_as_int
    else:
        # Otherwise, call this function again recursively
        return get_number()

def main_game():
    '''
    Play a round of the game.
    '''
    # Pick random number between MINIMUM and MAXIMUM
    goal = randint(MINIMUM, MAXIMUM)
    # Initially, the user hasn't guessed anything.
    user_guess = None

    print_welcome()
    # Repeatedly ask the user until they get it right
    while user_guess != goal:
        user_guess = get_number()
        process_guess(user_guess, goal)
    print_ending()

# This if statement is common in most professional Python
#   programs - don't worry too much about what it does,
#   but you can safely assume it will work when you press
#   the run button.
if __name__ == '__main__':
    main_game()