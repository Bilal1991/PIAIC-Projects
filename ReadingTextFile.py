import os
import sys

def insert_line_para_nums(infile):
    f = open(infile, 'r')
    linecount = 0
    paragraphcount = 0
    empty = True
    for i in f:
        if '\n' in i:
            linecount += 1
            if len(i) < 2:
                empty = True
            elif len(i) > 2 and empty is True:
                paragraphcount = paragraphcount + 1
                empty = False
    f.close()
    print("paragraphcount {} \n".format(paragraphcount))


def parse_file(path):

    fd = open(path,'r')
    spaces = tabs = words = num_lines = Total_chracters = special_chracter = 0
    lines_in_file = fd.read()
    Total_chracters = len(lines_in_file)
    words = len(lines_in_file.split())
    num_lines = lines_in_file.count('\n') +1
    #print ( "Number of Words: ", num_lines )
    tabs = len(lines_in_file.split('  ')) -1
    spaces = len(lines_in_file.split(' ')) -1
    special_chracter = Total_chracters - spaces - tabs
    #print ( "Number of SC: ", special_chracter)
    #print ( "Number of spaces: ", spaces - tabs * 2)
    #for i,line in enumerate(fd):
        #spaces += line.count(' ')
        #tabs += line.count('  ')
    #Now close the open file
    fd.close()

    #Return the result as a tuple
    return spaces - tabs * 2, tabs,num_lines,words,special_chracter
    


fileNames = list(input("please enter comma seperated file name: eg; file1.txt,file2.txt \n").split(','))
#print(fileNames)
for fileName in fileNames:
    if os.path.isfile(fileName) is True:
        
        spaces, tabs, lines,words,special_chracter = parse_file(fileName)
        print("Details of the file {} is given below:".format(fileName))
        print ("\n Spaces {} \n tabs {} \n lines {} \n words {} \n non space chracters {}".format (spaces, tabs, lines,words,special_chracter))
        insert_line_para_nums(fileName)    
    else :
        print(fileName, "Not exists")