'''
Created on Apr 27, 2015

@author: dcsliub
'''

import os
from bs4 import BeautifulSoup
import re

class IEEEExtractor:
    
    def __init__(self):
        self.punctuation = [".", ",", ")", "(", "?", ":", "'", "\"", ";"]
        self.dgwList = ["eg", "et", "al", "etc"]
    
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
                for punct in self.punctuation:
                    if punct in word:
                        word = word.replace(punct, "")
                #for
                         
                if "-" in word:
                    subWords = word.split("-")
                    word = ""
                    for subWord in subWords:
                        if subWord.isalpha():
                            word = word + subWord + " "
                     
                if (" " not in word) and (not word.isalpha()):                #English word
                    continue;
                             
                for dgw in self.dgwList:                   #DGW
                    if word == dgw:
                        word = ""
                        break;
                             
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

conference = "iccv"
rootDir = r"C:\Users\dcsliub\Desktop\abstactdata" + "\\" + conference
textDirName = "text"
abstractDirName = "abstract"
yearList = ["13", "11", "09", "07", "05", "03"]

for year in yearList:
    textDir = os.path.join(rootDir, textDirName, year)
    abstractDir = os.path.join(rootDir, abstractDirName, year)

    ieeeExtractor = IEEEExtractor()
    ieeeExtractor.extractFromIEEE(textDir, abstractDir, conference, year)
print("Program ends")
