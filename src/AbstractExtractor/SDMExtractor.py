# -*- coding: utf-8 -*-
'''
Created on Apr 27, 2015

@author: dcsliub
'''

import os
from bs4 import BeautifulSoup

class SDMExtractor:
    
    def __init__(self):
        self.punctuation = [".", ",", ")", "(", "?", ":", ";", "'", "\"", "-", "#", "$", "&", 
                       "^", "%", "*", "@", "`", "~", "/", "<", ">", "[", "]", "|", "=", "+", "_", "!"
                       "{", "}", "\\"]
        self.dgwList = ["e.g.", "et al", ".etc", "iii","ii", "i.e.", "(ie)", "(ie"]
    
    def extractSDM(self, textDir, abstractDir, year, conference):
        
        if not os.path.exists(abstractDir):
            os.mkdir(abstractDir)
            
        num = 0
        for file in os.listdir(textDir):
            filePath = os.path.join(textDir, file)

            content = open(filePath, "r").read()

            soup = BeautifulSoup(content)
            div = soup.findAll('div', attrs={'class':'abstractSection'})
            if len(div) < 2:
                continue
            
            pList = div[1].findAll('p')
            #if len(pList) > 1:
                #print(pList[0].text)
                    
            if not pList is None and len(pList) > 0:
                abstract = ""
                for p in pList:
                    text = p.text
                    words = text.strip().lower().split()
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
                    #for word
                    abstract = abstract + newText + " "
                #for p
                try:
                    file = os.path.join(abstractDir, conference + year + str(num) + ".txt")
                    fileHandler = open(file, "w")
                    fileHandler.write(abstract)
                    fileHandler.close()
                except:
                    print(file)
            #if
            
            print(num)
            num = num + 1
        #for
    #def
#class

acmExtractor = SDMExtractor()
conference = "sdm"
yearList = ["14", "13", "12", "11", "10", "09"]
rootDir = r'C:\Users\dcsliub\Desktop\HierarchyData\abstactdata' +'\\' + conference 

textDirName = "text"
abstractDirName = "abstract"

for year in yearList:
    textDir = os.path.join(rootDir, textDirName, year)
    abstractDir = os.path.join(rootDir, abstractDirName, year)
    acmExtractor.extractSDM(textDir, abstractDir, year, conference)
#for
print("Program ends")