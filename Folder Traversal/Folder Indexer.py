# Levent DURDALI
# 9.07.2019
# Give all folder names in the specified folder


import os
import tkinter as tk
from tkinter import filedialog
from datetime import date

today = date.today()

root = tk.Tk()
root.withdraw()
dirname = filedialog.askdirectory(
    parent=root, initialdir="/", title="Please select a directory"
)  # select a directory
folder_name = os.path.basename(dirname)  # Get directory name
dir_list = next(os.walk(dirname))[1]  # Get all folder names


file1 = open("%s.txt" % (folder_name), "w") # Create a text file with the folder name

x = 1
for fileName in dir_list: # Write all folder names in the text file
    file1.write("{} \t".format(x)) # Write the folder number
    file1.write(fileName + "\n") # Write the folder name
    x = x + 1 # Increase the folder number
file1.close() # Close the text file


with open("%s.txt" % (folder_name), "r") as contents: # Read the text file
    save = contents.read() # Read the text file
with open("%s.txt" % (folder_name), "w") as contents:
    x = x - 1
    date = today.strftime("%B %d, %Y") # Get the current date
    contents.write(" \n\n") # Write a new line
    contents.write("{} \nTotal number of folders are {} \n \n".format(date, x)) # Write the current date and the total number of folders
with open("%s.txt" % (folder_name), "a") as contents: # Append the text file
    contents.write(save) # Append the text file
    file1.close() # Close the text file
file1.close()
