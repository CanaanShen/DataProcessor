'''
Created on Apr 27, 2015

@author: dcsliub
'''

import os
from bs4 import BeautifulSoup
import urllib.request

class ACMExtractor:
    
    def extractAbstract(self, textDir, abstractDir, year, conference):
        punctuation = [".", ",", ")", "(", "?", ":", "-"]
        dgwList = ["eg", "et", "al", "etc"]
        
        if not os.path.exists(abstractDir):
            os.mkdir(abstractDir)
            
        for file in os.listdir(textDir):
            filePath = os.path.join(textDir, file)
            print(filePath)
#             opener = urllib.request.urlopen(filePath)
#             content = opener.read()
            content = open(filePath, "r").read()
#             content = content.decode('utf-8').encode('cp850', 'replace').decode('cp850')

            soup = BeautifulSoup(content)
            divList = soup.findAll('div', attrs={'style':'display:inline'})
            num = 0
            for div in divList:
                pList = div.findAll('p')
                if len(pList) > 1:
                    print(pList[0].text)
                    
                if not pList is None and len(pList) > 0:
                    abstract = ""
                    for p in pList:
                        text = p.text
                        words = text.strip().lower().split()
                        newText = ""
                        for word in words:
                            for punct in punctuation:
                                if punct in word:
                                    word = word.replace(punct, "")
                            #for
                        
                            if not word.isalpha():                #English word
                                continue;
                            
                            for dgw in dgwList:                   #DGW
                                if word == dgw:
                                    word = ""
                                    break;
                            
                            newText = newText + word + " ";
                        #for
                        abstract = abstract + newText + " "
                    #for
                    
                    file = os.path.join(abstractDir, conference + year + str(num) + ".txt")
                    fileHandler = open(file, "w")
                    fileHandler.write(abstract)
                    fileHandler.close()
                    print(num)
                    num = num + 1
                #if
            #for
    #def
#class

acmExtractor = ACMExtractor()
conference = "acl"
year = "09"
rootDir = r'C:\Users\dcsliub\Desktop\abstactdata' +'/' + conference 

textDirName = "text"
abstractDirName = "abstract"
textDir = os.path.join(rootDir, textDirName, year)
abstractDir = os.path.join(rootDir, abstractDirName, year)

acmExtractor.extractAbstract(textDir, abstractDir, year, conference)
print("Program ends")