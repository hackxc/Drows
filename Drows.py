#!/usr/bin/python
#-*- coding:utf-8 -*-
import subprocess,sys
from optparse import OptionParser
import os

def powershell(file,line):
    try:
        Newfile =file.split(".")[1]
        args = [r"powershell", r"Get-Content %s | Select-Object -Skip %s | Set-Content Newfile.%s" %(file, line,Newfile)]
        subprocess.call(args)
        print ("ok!")
    except:
        pass

def main():
    #Drows
    #http://www.hackxc.cc
    print ('''
 ____                        
|  _ \ _ __ _____      _____ 
| | | | '__/ _ \ \ /\ / / __|
| |_| | | | (_) \ V  V /\__ \\
|____/|_|  \___/ \_/\_/ |___/
''')
    try:
        print ("")
        usage = ("Usage : %prog -f <filename> -l <line>")
        parser = OptionParser(usage=usage)
        parser.add_option("-f","--file",dest="filename",help="The target filename")
        parser.add_option("-l", "--line", dest="line", help="The Delete rows")
        (options,args)=parser.parse_args()
        file = options.filename
        line = options.line
        if file == None or line == None:
            print ("Usage : %s -f <filename> -l <line>"%os.path.basename(sys.argv[0]))
            sys.exit(0)
        if file:
            if not os.path.exists(file):
                print ("File does not exist!")
                sys.exit(0)
        powershell(file,line)
    except:
        pass

if __name__ == '__main__':
   main()