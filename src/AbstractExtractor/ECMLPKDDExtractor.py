'''
Created on May 5, 2015

@author: dcsliub
'''

import os
import re
from bs4 import BeautifulSoup

class ECMLPKDDExtractor:
    
    def __init__(self):
        self.punctuation = [".", ",", ")", "(", "?", ":", ";", "'", "\"", "-", "#", "$", "&", 
                       "^", "%", "*", "@", "`", "~", "/", "<", ">", "[", "]", "|", "=", "+", "_", "!"
                       "{", "}", "\\"]
        self.dgwList = ["e.g.", "et al", ".etc", "iii","ii", "i.e.", "(ie)", "(ie"]
    
    def crawlECML14(self, textDir, abstractDir, year, conference):
    
        if not os.path.exists(abstractDir):
            os.mkdir(abstractDir)
    
        num = 0
        for file in os.listdir(textDir):
            filePath = os.path.join(textDir, file)
            fileHandler = open(filePath, "r")

            content = fileHandler.read()
            soup = BeautifulSoup(content)
            allTable = soup.findAll('table', attrs={'class':'table-accepted'})

            for eachTable in allTable:
                abstract = ""
                allP = eachTable.find_all('p')
                if len(allP) < 2:
                    continue
        
                abstract = allP[1].text.strip("\n").strip().lower().split()
                newAbstract = ""
                for word in abstract:
                    word  = word.lower()
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
                        
                        regex = re.compile("\\w+")
                        if regex.match(blankWord):                #English word
                            word = word + blankWord + " "
                    #for blankWord
                    newAbstract = newAbstract + word + " "
                #for word
                
                try:
                    file = os.path.join(abstractDir, conference + year + str(num) + ".txt")
                    fileHandler = open(file, "w")
                    fileHandler.write(newAbstract)
                    fileHandler.close()
 
                except:
                    print(str(num) + " exception")
            
                num = num + 1
            #for eachTable
        #for file
    #def
#class


if __name__ == "__main__":

    ecmlExtractor = ECMLPKDDExtractor()

    yearList = ["14"]
    conference = "ecml"

    rootDir = r"C:\Users\dcsliub\Desktop\HierarchyData\abstactdata" + "\\" + conference
    textDirName = "text"
    abstractDirName = "abstract"
    
    for year in yearList:
        textDir = os.path.join(rootDir, textDirName, year)
        abstractDir = os.path.join(rootDir, abstractDirName, year)
        
        if year == "14":
            ecmlExtractor.crawlECML14(textDir, abstractDir, year, conference)
    #for

    print("Program ends")