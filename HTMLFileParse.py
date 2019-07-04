from html.parser import HTMLParser
import os
import sys

dictionarTags ={}
dictionaryCloseTags ={}
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        #print("Encountered a start tag:", tag)
        if tag not in dictionarTags:
            dictionarTags[tag] = 1
        else:
            dictionarTags[tag]  +=1    
    def display (self):  
        print("\n Opening tags dictionary : {}".format(dictionarTags))
        print("\n Closing tags dictionary : {}".format(dictionaryCloseTags))
    def handle_endtag(self, tag):
        if tag not in dictionaryCloseTags:
            dictionaryCloseTags[tag] = 1
        else:
            dictionaryCloseTags[tag]  +=1 

    #def handle_data(self, data):
     #   if data not in dictionarTags:
      #      dictionarTags[data] = 1
       # else:
        #    dictionarTags[data]  +=1 
        
fileNames = list(input("please enter comma seperated html file name: eg; file1.html,file2.html \n").split(','))
#print(fileNames)
for fileName in fileNames:
    if os.path.isfile(fileName) is True:
        parser = MyHTMLParser()
        f = open(fileName, 'r')
        data = f.read()
        #print(type(data))
        print("Tags Parsing of file {} :".format(fileName))
        parser.feed(data)
        parser.display() 
        dictionarTags ={}
    else :
        print(fileName, "Not exists")
       