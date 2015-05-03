'''
Created on Apr 27, 2015

@author: dcsliub
'''

import os
from bs4 import BeautifulSoup
import re

class ICDMExtractor:
    
    def __init__(self):
        self.punctuation = [".", ",", ")", "(", "?", ":", ";", "'", "\"", "-", "#", "$", "&", 
                       "^", "%", "*", "@", "`", "~", "/", "<", ">", "[", "]", "|", "=", "+", "_", "!"
                       "{", "}", "\\"]
        self.dgwList = ["e.g.", "et al", ".etc", "iii","ii", "i.e.", "(ie)", "(ie"]
    
    def extractICDM(self, textDir, abstractDir, conference, year):
    
        if not os.path.exists(abstractDir):
            os.mkdir(abstractDir)
            
        num = 0
        for eachFile in os.listdir(textDir):
            eachFilePath = os.path.join(textDir, eachFile)
            eachFileHandler = open(eachFilePath, "r")
            content = eachFileHandler.readlines()
                
            if content == '' or len(content) == 0:   #nothing
                continue
                    
            abstract = ""
            for line in content:
                words = line.strip("\n").strip().lower().split()
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
                        if blankWord != "k" and blankWord != "a" and blankWord!= "x" and len(blankWord) == 1:
                            blankWord = ""
                            
                        if blankWord.isalpha():                #English word
                            word = word + blankWord + " "
                    #for blankWord
                    
                    abstract = abstract + word + " "
                #for word
            #for line
            outFilePath = os.path.join(abstractDir, conference + year + str(num) + ".txt")
            outFileHandler = open(outFilePath, "w")
            outFileHandler.write(abstract)
            outFileHandler.close()
            print(num)
            num = num + 1
        #for eachFile
    #def
#class

conference = "icdm"
rootDir = r"C:\Users\dcsliub\Desktop\HierarchyData\abstactdata" + "\\" + conference
textDirName = "text"
abstractDirName = "abstract"
yearList = ["14"]

for year in yearList:
    textDir = os.path.join(rootDir, textDirName, year)
    abstractDir = os.path.join(rootDir, abstractDirName, year)

    jmlrExtractor = ICDMExtractor()
    jmlrExtractor.extractICDM(textDir, abstractDir, conference, year)
print("Program ends")
