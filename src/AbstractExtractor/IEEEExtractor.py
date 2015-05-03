'''
Created on Apr 27, 2015

@author: dcsliub
'''

import os
from bs4 import BeautifulSoup
import re

class IEEEExtractor:
    
    def __init__(self):
        self.punctuation = [".", ",", ")", "(", "?", ":", ";", "'", "\"", "-", "#", "$", "&", 
                       "^", "%", "*", "@", "`", "~", "/", "<", ">", "[", "]", "|", "=", "+", "_", "!"
                       "{", "}", "\\"]
        self.dgwList = ["e.g.", "et al", ".etc", "iii","ii", "i.e.", "(ie)", "(ie"]
    
    def extractFromIEEE(self, textDir, abstractDir, conference, year):
        
        if not os.path.exists(abstractDir):
            os.mkdir(abstractDir)
        
        num= 0
        for file in os.listdir(textDir):
            filePath = os.path.join(textDir, file)
            regular = re.compile(r"icp.jsp_arnumber=\d+_page=2.html")
            if not regular.match(file):
                continue
            
            content = open(filePath, "r").read()
 
            soup = BeautifulSoup(content)
            div = soup.find('div', attrs={'class':'text'})
            if div is None or len(div) <= 0:
                continue
            
            p = div.find('p')
            
            if p is None or len(p) <= 0:
                continue
            
            pText = p.text
            words = pText.strip().lower().split()
            abstract = ""
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
                             
                abstract = abstract + word + " ";
            #for word
                                 
            file = os.path.join(abstractDir, conference + year + str(num) + ".txt")
            fileHandler = open(file, "w")
            fileHandler.write(abstract)
            fileHandler.close()
            print(num)
            num = num + 1
        #for file
    #def
#class

conference = "icdm"
rootDir = r"C:\Users\dcsliub\Desktop\HierarchyData\abstactdata" + "\\" + conference
textDirName = "text"
abstractDirName = "abstract"
yearList = ["13", "11", "12", "10", "09"]
# yearList = ["14", "12", "10", "09"]
ieeeExtractor = IEEEExtractor()

for year in yearList:
    textDir = os.path.join(rootDir, textDirName, year)
    abstractDir = os.path.join(rootDir, abstractDirName, year)
    print(textDir)
    ieeeExtractor.extractFromIEEE(textDir, abstractDir, conference, year)
print("Program ends")
