import random
def number(x):
    low=0
    high=x
    feedback=""

    while feedback != "c":
        guess=random.randint(low,high)
        feedback=input(f"Is {guess} too high type h, too low type l or correct type c ")
        if feedback=="h":
            high=guess-1
        elif feedback=="l":
            low=guess+1
    print(f"Yahoo yout computer guess the correct number {guess}")
number(20)

'''                                      Mohammad Usman
                                        23/10/2021
                                        '''