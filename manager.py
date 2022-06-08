# TODO - split the menu into its own file from manager
from generator import *
from steal_user_data import *
import os

def savePassword(website, password):
    # securely save password
    file = open(".super_secure_password_file", "a")
    file.write(website + "\t" + password + "\n")
    file.close()
    
def readPasswords():
    passwordDict = {}
    with open(".super_secure_password_file") as file:
        for line in file:
            website, password = line.split("\t")
            if website not in passwordDict:
                passwordDict[website] = password
            else:
                passwordDict.update({website: password})
    return passwordDict


# os.system('clear' if os.name =='posix' else 'cls')
# print("M64 Password Management System ----------")
# print("1. Generate new password")
# print("2. View passwords")
# print("3. Exit program")
# choice = input(": ")

# while True:

#     if choice == '1':
#         length = input("How many characters should the password be? ")
#         if int(length) < 4:
#             print("How about you come back when you have a real request?")
#             break
#         password = generate(length)

#         choice = input("Would you like to save this password? (Y/N): ")
#         if choice == 'y' or choice == 'Y':
#             name = input("What website is this password for? ")
#             savePassword(name, password)
#         break

#     elif choice == '2':
#         readPasswords()
#         choice = input(": ")

#     elif choice == '3':
#         print("goodbye!")
#         break
#         # this is done perfectly well done

#     else: 
#         print("incorrect option")
#         choice = input(": ")