def diary():

    ask_qus = input("Would you like to read (r) or write (w) to your diary? ")

    if ask_qus == "r":

        new_file = open('C:/Users/k1509041/Desktop/newfile/notes.txt', 'r')

        print(new_file.read())

        new_file.close()



    else:

        new_file = open('C:/Users/k1509041/Desktop/newfile/notes.txt', 'a')

        new_entry = input("What would you like to add to your diary? ")

        new_file.write(new_entry)

        new_file.close()
