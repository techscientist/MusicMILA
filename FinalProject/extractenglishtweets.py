import glob
import os,fnmatch
import sys
import glob
import string
import re
import random
from guess_language import guess_language
import json as simplejson

def recursive_glob(treeroot, pattern):
    results = []
    for base, dirs, files in os.walk(treeroot):
        goodfiles = fnmatch.filter(files, pattern)
        results.extend(os.path.join(base, f) for f in goodfiles)
    return results

def main():
    rootdirname = sys.argv[1]
    #read all the files in the directory with .txt extension
    print(rootdirname)
    listfiles =  recursive_glob(rootdirname,"*.txt") 
    if len(listfiles) == 0:
        print ("No files present")
        sys.exit(1)

    i = 0
    randfileslist = random.sample(listfiles,25)
    for file in randfileslist:
        print ("Current file is :",file)
        f = open(file, "r")
        lines = f.readlines()
        txtfile = open('tweetdata.txt',mode ='at')
        for line in lines:	
            try:
                tweet = simplejson.loads(line)
                if "text" in tweet:
                    text = str(tweet["text"].encode('utf-8','ignore'))
                    language = guess_language(text)
                    if language == 'en':
                        i = i +1
                        if i == 501:
                            i = 0
                            break
                        txtfile.write(line)
            except ValueError:
                pass
		


if __name__ == '__main__':
    main()
