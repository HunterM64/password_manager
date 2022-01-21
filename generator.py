from operator import truediv
import string
import random
import pyperclip as pc
possible_chars = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate(length):
    
    assword = random.choice(possible_chars)
    for _ in range (int(length)-1):
        # construct password from possible characters
        assword += random.choice(possible_chars)

    # make sure our password has an upper, lower, number, and special char
    lower, upper, digit, special = False, False, False, False
    for c in assword:
        if c in string.ascii_lowercase:
            lower = True
        elif c in string.ascii_uppercase:
            upper = True
        elif c in string.digits:
            digit = True
        elif c in "!@#$%^&*()":
            special = True

    # if there isn't one of each, generate new password
    if (not lower or not upper or not digit or not special):
        generate(length)
    else:
        print("Your password is: " + assword)
    
        # copy password to clipboard
        pc.copy(assword)
        print("This has been copied to your clipboard.")

        return assword

    

    

