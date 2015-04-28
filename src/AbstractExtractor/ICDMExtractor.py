'''
Created on Apr 27, 2015

@author: dcsliub
'''

import os
from bs4 import BeautifulSoup
import re

class ICDMExtractor:
    
    def extractICDM(self, textDir, abstractDir, conference, year):
        
        punctuation = [".", ",", ")", "(", "?", ":"]
        dgwList = ["eg", "et", "al", "etc"]
    
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
                        
                    for punct in punctuation:
                        if punct in word:
                            word = word.replace(punct, "")
                    #for
                    
                    if "-" in word:
                        subWords = word.split("-")
                        word = ""
                        for subWord in subWords:
                            word = word + " " + subWord
                    
                    if (" " not in word) and (not word.isalpha()):                #English word
                        continue;
                    
                    for dgw in dgwList:                   #DGW
                        if word == dgw:
                            word = ""
                            break;
                    #for
                    
                    abstract = abstract + word + " "
                #for
            #for
            outFilePath = os.path.join(abstractDir, conference + year + str(num) + ".txt")
            outFileHandler = open(outFilePath, "w")
            outFileHandler.write(abstract)
            outFileHandler.close()
            print(num)
            num = num + 1
            #for
    #def
    
    def extractFromIEEE(self, textDir, abstractDir, conference, year):
        
        punctuation = [".", ",", ")", "(", "?", ":", "-"]
        dgwList = ["eg", "et", "al", "etc"]
        
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
            pText = div.find('p').text
 
            words = pText.strip().lower().split()
            abstract = ""
            for word in words:
                for punct in punctuation:
                    if punct in word:
                        word = word.replace(punct, "")
                #for
                         
                if "-" in word:
                    subWords = word.split("-")
                    word = ""
                    for subWord in subWords:
                        word = word + " " + subWord
                     
                if (" " not in word) and (not word.isalpha()):                #English word
                    continue;
                             
                for dgw in dgwList:                   #DGW
                    if word == dgw:
                        word = ""
                        break;
                             
                abstract = abstract + word + " ";
            #for
                                 
            file = os.path.join(abstractDir, conference + year + str(num) + ".txt")
            fileHandler = open(file, "w")
            fileHandler.write(abstract)
            fileHandler.close()
            print(num)
            num = num + 1
        #for
    #def
#class

conference = "icdm"
rootDir = r"C:\Users\dcsliub\Desktop\abstactdata" + "\\" + conference
textDirName = "text"
abstractDirName = "abstract"
year = "09"
textDir = os.path.join(rootDir, textDirName, year)
abstractDir = os.path.join(rootDir, abstractDirName, year)

jmlrExtractor = ICDMExtractor()
jmlrExtractor.extractFromIEEE(textDir, abstractDir, conference, year)
print("Program ends")
