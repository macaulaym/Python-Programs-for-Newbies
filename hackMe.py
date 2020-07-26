import os

#allows you to delete dir and all files inside it
import shutil

import time

time.sleep(2)

os.mkdir(r'C:/Users/avaguest/Desktop/PleaseOpenMe!')

file = open ("C:/Users/avaguest/Desktop/PleaseOpenMe!/innocent.txt", "w")

file.write("You've been hacked - HAHA!!!")

file.close()

time.sleep(30)

#deletes dir and all files inside it
shutil.rmtree('C:/Users/avaguest/Desktop/PleaseOpenMe!')
