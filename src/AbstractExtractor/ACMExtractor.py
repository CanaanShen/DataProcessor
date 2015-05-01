'''
Created on Apr 27, 2015

@author: dcsliub
'''

import os
import re
from bs4 import BeautifulSoup

class ACMExtractor:
    
    def __init__(self):
        self.punctuation = [".", ",", ")", "(", "?", ":", ";", "'", "\"", "-", "#", "$", "&", 
                       "^", "%", "*", "@", "`", "~", "/", "<", ">", "[", "]", "|", "=", "+", "_", "!"
                       "{", "}", "\\"]
        self.dgwList = ["e.g.", "et al", ".etc", "iii","ii", "i.e.", "(ie)", "(ie"]
    
    def extractAbstract(self, textDir, abstractDir, year, conference):
        
        if not os.path.exists(abstractDir):
            os.mkdir(abstractDir)
        
        num = 0
        for file in os.listdir(textDir):
            filePath = os.path.join(textDir, file)
            print(filePath)

            content = open(filePath, "r").read()

            soup = BeautifulSoup(content)
            divList = soup.findAll('div', attrs={'style':'display:inline'})
            
            divLen = len(divList)
            print("total div number: ", str(divLen))
            for div in divList:
                pList = div.findAll('p')
#                 if len(pList) > 1:
#                     print(pList[0].text)
                
                if conference != "vldb" and conference != "wsdm" and num > (divLen/2 - 8):   #workshop or address
                    break;
                
                if conference == "wsdm" and num > (divLen/2- 3):
                    break;
                
                if not pList is None and len(pList) > 0:
                    abstract = ""
                    for p in pList:
                        originalText = ""
                        for content in p.contents:
                            if "<u>" in str(content):
                                content = content.replace("<u>", " ")
                                content = content.replace("</u>", " ")
                            
                            if ">" in str(content) and "</" in str(content):
                                originalText = originalText + " " + content.text  #tag
                            else:
                                originalText = originalText + " " + content       #text
                        #for

                        words = originalText.strip().lower().split()
                        newText = ""
                        for word in words:
                            for dgw in self.dgwList:                   #DGW
                                if dgw in word or dgw == word:
                                    word = word.replace(dgw, " ")
                                    break;
                            #for dgw
                    
                            for punct in self.punctuation:
                                if punct in word:
                                    word = word.replace(punct, " ")
                            #for punct
                        
                            blankWords = word.split()
                            word = ""
                            for blankWord in blankWords:
                                if blankWord != "k" and len(blankWord) == 1:
                                    blankWord = ""
                            
                                if blankWord.isalpha():                #English word
                                    word = word + blankWord + " "
                            #for blankWord
                             
                            newText = newText + word + " ";
                        #for
                        abstract = abstract + newText + " "
                    #for p in pList
                    
                    try:
                        file = os.path.join(abstractDir, conference + year + str(num) + ".txt")
                        fileHandler = open(file, "w")
                        fileHandler.write(abstract)
                        fileHandler.close()
                    except:
                        print(Exception)
                    num = num + 1
                    print(num)
                #if not p is None and ...
            #for div
        #for file
    #def

    def extractAbstractICDE(self, textDir, abstractDir, year, conference):
        
        if not os.path.exists(abstractDir):
            os.mkdir(abstractDir)
        
        num = 0
        for file in os.listdir(textDir):
            
            filePath = os.path.join(textDir, file)
            print(filePath)

            content = open(filePath, "r").read()

            soup = BeautifulSoup(content)
            spanList = soup.findAll('span', id=re.compile('toHide\\d+'))
                        
            spanLen = len(spanList)
            print("total span number: ", str(spanLen))
            for span in spanList:
                
                if conference != "vldb" and conference != "wsdm" and num > (spanLen - 10):
                    break;
                
                div = span.find('div', style='display:inline')

                originalText = ""
                for content in div.contents:
                            
                    if ">" in str(content) and "</" in str(content):
                        originalText = originalText + content.text + " " #tag
                    else:
                        originalText = originalText + content + " " #text
                #for content
                
                abstract = ""
                words = originalText.strip().lower().split()
                for word in words:
                    for dgw in self.dgwList:                   #DGW
                        if dgw in word or dgw == word:
                            word = word.replace(dgw, " ")
                            break;
                    #for dgw
                    
                    for punct in self.punctuation:
                        if punct in word:
                            word = word.replace(punct, " ")
                    #for punct
                        
                    blankWords = word.split()
                    word = ""
                    for blankWord in blankWords:
                        if blankWord != "k" and len(blankWord) == 1:
                            blankWord = ""
                            
                        if blankWord.isalpha():                #English word
                            word = word + blankWord + " "
                    #for blankWord
                             
                    abstract = abstract + word + " ";
                #for word
                    
                try:
                    file = os.path.join(abstractDir, conference + year + str(num) + ".txt")
                    fileHandler = open(file, "w")
                    fileHandler.write(abstract)
                    fileHandler.close()
                except:
                    print(Exception)
                num = num + 1
                print(num)
            #for span
        #for file
    #def
    
#class

acmExtractor = ACMExtractor()
conference = "www"
yearList = ["14", "13", "12", "11", "10", "09"]
rootDir = r'C:\Users\dcsliub\Desktop\HierarchyData\abstactdata' +'\\' + conference 

textDirName = "text"
abstractDirName = "abstract"

for year in yearList:
    textDir = os.path.join(rootDir, textDirName, year)
    abstractDir = os.path.join(rootDir, abstractDirName, year)
    
    if conference == "icde":
        acmExtractor.extractAbstractICDE(textDir, abstractDir, year, conference)
    else:
        acmExtractor.extractAbstract(textDir, abstractDir, year, conference)
#for
print("Program ends")