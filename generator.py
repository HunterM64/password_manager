from operator import truediv
import string
import random
import pyperclip as pc
possible_chars = list(string.ascii_letters + string.digits + "!@#$%^&*()")

""" generates a password of characters equalling to given length """
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
        if c in string.ascii_uppercase:
            upper = True
        if c in string.digits:
            digit = True
        if c in "!@#$%^&*()":
            special = True

    print(lower and upper and digit and special)

    if (lower and upper and digit and special):
        # done
        pc.copy(assword)
        return assword
    else:
        # try again
        return generate(length)

    

    

