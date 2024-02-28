# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes or no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes or no")


def instructions():
    print('''
 
 **** Instructions ****
 
To begin, decide on a score goal (eg: First one to get a 
score of 50 wins). 

For each round of the game, you win points by rolling dice.
At the start of each round, the player and the computer each roll two dice
and thereafter one. 

The winner of the round is the first person who gets 13 points or less, you cannot go over 13.
If you go over 13 you lose the round and do not get any points.

If you win the round, your score will increase by the
number of points that you earned. If your first roll of two
dice is a double (eg:both dice show a six), then your score will be 
DOUBLE the number of points (2 6's = 12, 12 x 2 = 24 points)

If you and the computer tie (eg: you both get a score of 10),
then you will have 10 points added to your score.

Your goal is to get to the target score before the computer.

Good luck.

    ''')


# Main routine
print()
print("🎲🎲 Roll it 13 🎲🎲")
print()

# loop for testing purposes

want_instructions = yes_no("Do you want to read the instructions? (Enter yes or no) ")

# checks users enter (y) or (n)
if want_instructions == "yes":
    instructions()

print("program continues")
