# Check that users have entered a valid
# option based on a list
def rps_compare(user, comp):

    # If the user and the computer choice is the same, it's a tie
    if user == comp:
        result = "tie"

    # There are three ways to win
    elif user == "paper" and comp == "rock":
        result = "win"
    elif user == "scissors" and comp == "paper":
        result = "win"
    elif user == "rock" and comp == "scissors":
        result = "win"

    # if it's not a win / tie, then it's a loss
    else:
        result = "lose"

    return result


# Automated testing is below in the form (test_case, expected_value)
to_test = [
    ('rock', 'rock', 'tie'),
    ('rock', 'paper', 'lose'),
    ('rock', 'scissors', 'win'),
    ('paper', 'rock', 'win'),
    ('paper', 'paper', 'tie'),
    ('paper', 'scissors', 'lose'),
    ('scissors', 'rock', 'lose'),
    ('scissors', 'paper', 'win'),
    ('scissors', 'scissors', 'tie'),
]


for item in to_test:
    # retrieve test case and expected value
    user = item[0]
    comp = item[1]
    expected = item[2]

    # get actual value (ie: test ticket function)
    actual = rps_compare(user, comp)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f" ✅✅✅Passed! Case: {user} vs {comp}, expected: {expected} received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {user} vs {comp}, expected: {expected} received: {actual} ❌❌❌")
