import string
import random
possible_chars = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate(length):
    assword = random.choice(possible_chars)
    for _ in range (int(length)-1):
        assword += random.choice(possible_chars)
    print("Your password is: " + assword)

    # TODO: copy password to clipboards

    print("This has NOT been copied to your clipboard.")

length = input("How many characters should the password be? ")
generate(length)

