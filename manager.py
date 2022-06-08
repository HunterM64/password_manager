""" Saves password to .super_secure_password_file"""
def savePassword(website, password):
    # securely save password
    file = open(".super_secure_password_file", "a")
    file.write(website + "\t" + password + "\n")
    file.close()
    
""" Reads passwords from file, saves to dictionary and returns said dictionary """
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