# You should create a text document on the desktop called: demo_password_database_windows
#This program will insert newly created credentials in this document, while hashing the password.

from random import randint

dPath = 'C:\\Users\\avaguest\\Desktop'
dFilename = 'demo_password_database_windows.txt'

def create_database(path=dPath, filename=dFilename):
    data_file = open(path + '\\' + filename, 'w')
    data_file.close()

def create_new_account(name, password, path=dPath, filename=dFilename):
    # Creates a record which consists of the name, the salt, and the
    # hashed and salted password, separated by '|'s.
    data_file = open(path + '\\' + filename, 'a')
    data_file.write(str(name)+'|')
    newSalt = randint(0, (2**32)-1)
    data_file.write(str(newSalt)+'|')
    data_file.write(str(hash(str(newSalt)+password))+'|\n')
    data_file.close()
    print('Account for "%s" created sucessfully.' % name)

def get_parts(text, sep='|', ignore=('\n',)):
    holder = ''
    parts = []
    for c in text:
        if c not in ignore:
            if c == sep:
                parts += [holder]
                holder = ''
            else:
                holder += c
    parts += [holder]
    return parts

def validate_password(name, password, path=dPath, filename=dFilename):
    data_file = open(path + '\\' + filename, 'r')
    found = False
    correct = False
    while True:
        line = data_file.readline()
        parts = get_parts(line, '|', ('\n',))
        if parts[0] == name:
            found = True
            if str(hash(parts[1] + password)) == parts[2]:
                correct = True
            break
        elif line == '':
            break
        else:
            continue
    if found:
        if correct:
            print('Validated sucessfully.')
        else:
            print('Incorrect password.')
    else:
        print('User not found.')

def main():
    comm = input("Create database (D), create user (C), validate password (P), or exit (E): ")
    if comm in ('d','D'):
        create_database()
    elif comm in ('c','C'):
        create_new_account(input("Enter new username: "),
                           input("Enter password: "))
    elif comm in ('p','P'):
        validate_password(input("Enter your username: "),
                          input("Enter your password: "))
    elif comm in ('e','E'):
        return 'exit'
    else:
        return 'contine'

while True:
    if main() == 'exit':
        break
