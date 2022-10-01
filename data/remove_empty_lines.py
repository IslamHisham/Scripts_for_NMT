#!/usr/bin/env python
# coding: utf-8

#from tempfile import mkstemp
#from shutil import move, copymode
#from os import fdopen, remove
import re
import sys
src_cleaned_file = sys.argv[1]
trgt_cleaned_file = sys.argv[2]
src_valid_cleaned_file = sys.argv[3]
trgt_valid_cleaned_file = sys.argv[4]

def compare(src_cleaned_file,trgt_cleaned_file,src_valid_cleaned_file,trgt_valid_cleaned_file):
    src_valid_cleaned_file = open(src_valid_cleaned_file, "x",encoding="utf8")
    trgt_valid_cleaned_file = open(trgt_valid_cleaned_file, "x",encoding="utf8")
    counter=0;

    with open(src_cleaned_file,"r",encoding="utf8") as f1, open(trgt_cleaned_file,"r",encoding="utf8") as f2:
        for line1, line2 in zip(f1, f2):
            if(line1.strip()=="" or line2.strip()==""):
                print("empty line1",line1)
                print("empty line2",line2)
                print("counter",counter)

            else:
                src_valid_cleaned_file.write(line1)
                trgt_valid_cleaned_file.write(line2)
            counter+=1
    print("final counter",counter)
    src_valid_cleaned_file.close()
    trgt_valid_cleaned_file.close()


if __name__ == '__main__':
    compare(src_cleaned_file,trgt_cleaned_file,src_valid_cleaned_file,trgt_valid_cleaned_file)