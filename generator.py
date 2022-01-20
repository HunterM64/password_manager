import string
import random
import pyperclip as pc
possible_chars = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate(length):
    
    assword = random.choice(possible_chars)
    
    for _ in range (int(length)-1):
        # construct password from possible characters
        assword += random.choice(possible_chars)
    
    print("Your password is: " + assword)
    
    # copy password to clipboard
    pc.copy(assword)
    print("This has been copied to your clipboard.")

    return assword

