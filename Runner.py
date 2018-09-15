import tkinter.filedialog as tkFileDialog
from tkinter import *
import subprocess
import re
import os

#filetypes = (
#        ("Python files", "*.py *.pyw", "TEXT"),
#        ("Text files", "*.txt", "TEXT"),
#        ("All files", "*"),
#        )
filetypes = (("DAT files","*.DAT"),)
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = tkFileDialog.askopenfilename(filetypes=filetypes)
#Must process files and folders to remove spaces since they parse as separate arguments.
#For example, 'C:/Users/My Games/Cool Game/' will be 3 command line arguments due to 2 spaces.
#This regex changes it to 'C:/Users/"My Games"/"Cool Game"/'
regex = "(?<=\/)[^\/]+\s[^\/]+(?=\/)"
replacement = "\"\g<0>\""
filename = re.sub(regex,replacement,filename)
subprocess.Popen("python -m xyppy " + filename)

