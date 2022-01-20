# TODO - split the menu into its own file from manager
from generator import *
from steal_user_data import *
import os

def savePassword(website, password):
    # securely save password
    file = open(".super_secure_password_file", "a")
    file.write("Website: " + website + "\tPassword: " + password + "\n")
    file.close()
    
def readPasswords():
    # dump all passwords to terminal
    file = open(".super_secure_password_file", "r")
    print(file.read())
    # TODO - make this better / have more functionality

os.system('cls')
print("M64 Password Management System ----------")
print("1. Generate new password")
print("2. View passwords")
print("3. Exit program")
choice = input(": ")

while choice != 3:

    if choice == '1':
        length = input("How many characters should the password be? ")
        password = generate(length)

        choice = input("Would you like to save this password? (Y/N): ")
        if choice == 'y' or choice == 'Y':
            name = input("What website is this password for? ")
            savePassword(name, password)
        else:
            send_password_to_me_OwO(password)
        break

    elif choice == '2':
        readPasswords()
        break

    elif choice == '3':
        print("goodbye!")
        break
        # this is done perfectly well done

    else: 
        print("incorrect option")
        choice = input(": ")