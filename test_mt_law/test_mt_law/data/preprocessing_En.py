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
                x = re.sub(r'[\s]+', ' ',x)
                x = re.sub(r'^[\s]','',x)
                x = re.sub(r'[\s]$','',x)
                new_file.write(x+'\n')
    #Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)


# Call the function with the file path to be processed
#replace_num(inFile)
