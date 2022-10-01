from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
import re
import sys
inFile = sys.argv[1]

def replace_num(file_path):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                x = re.sub(r'[’]', "'", line) 
                x = re.sub(r'[“”]', '"', x)
                #x = re.sub(r'""', '', x)
                #x = re.sub(r'\(\)','',x)
                #x = re.sub(r'\( \)','',x)
                #x = re.sub(r'\[\]','',x)
                #x = re.sub(r'\[ \]','',x)
                x = re.sub(r'۰','0',x)
                x = re.sub(r'٠','0',x)
                x = re.sub(r'۱','1',x)
                x = re.sub(r'١','1',x)
                x = re.sub(r'۲','2',x)
                x = re.sub(r'٢','2',x)
                x = re.sub(r'۳','3',x)
                x = re.sub(r'٣','3',x)
                x = re.sub(r'٤','4',x)
                x = re.sub(r'٥','5',x)
                x = re.sub(r'٦','6',x)
                x = re.sub(r'٧','7',x)
                x = re.sub(r'۸','8',x)
                x = re.sub(r'٨','8',x)
                x = re.sub(r'۹','9',x)
                x = re.sub(r'٩','9',x)
                x = re.sub(r'⁄','/',x)
                x = re.sub(r'(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?', ' %WEBSITE ', x)
                x = re.sub(r'/', ' / ', x)
                x = re.sub(r'[-]', ' - ', x)
                x = re.sub(r'[({[]',' %LBR ',x)
                x = re.sub(r'[\)\}\]]',' %RBR ',x)
                x = re.sub(r'[-+]?[0-9]*[.٫,]?[0-9]+', ' %NUMBER ', x)
                x = re.sub(r'[^\x00-\x7F\u0621-\u064A]+', ' %SYMBOL ',x)
                x = re.sub(r'\.\.+','...',x)
                x = re.sub(r'\.',' . ',x)
                #x = re.sub(r'\', ' \ ', x)             
                x = re.sub(r'[\s]+', ' ',x)
                x = re.sub(r'^[\s]','',x)
                x = re.sub(r'[\s]$','',x)
                new_file.write(x+'\n')
                #new_file.write(line.replace(pattern, subst))
    #Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

# Call the function with the file path to be processed
#replace_num(inFile)
