import random
"""
any_number=random.randint(1,10+1)
print(any_number)"""

"""
guess the c number that Generate by the computer 
""" 

def guess(x):
    random_number=random.randint(0,x)
    guess=0
    while guess!=random_number:
        guess=int(input(f"Guess a number between 1 and {x}"))
        if guess>random_number:
            print("Too High try again")
        elif guess<random_number:
            print("Too low try again")
        else:
            print("You have guess the correct number thaat generate by computer {}".format(random_number))


guess(50)