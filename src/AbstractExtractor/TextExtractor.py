'''
Created on Apr 26, 2015

@author: dcsliub
'''
import os
import re

class TextExtractor:
    
    def __init__(self):
        self.punctuation = [".", ",", ")", "(", "?", ":", ";", "'", "\"", "-", "#", "$", "&", 
                       "^", "%", "*", "@", "`", "~", "/", "<", ">", "[", "]", "|", "=", "+", "_", "!"
                       "{", "}", "\\"]
        self.dgwList = ["e.g.", "et al", "e.g", ".etc", "iii","ii", "i.e.", "(ie)", "(ie"]
        
    def extractFromText(self, textDir, abstractDir, conference, yearList):
        
        for subDir in yearList:
            subDirPath = os.path.join(textDir, subDir)
            outSubDirPath = os.path.join(abstractDir, subDir)
            if not os.path.exists(outSubDirPath):
                os.mkdir(outSubDirPath)
            
            num = 0
            for eachFile in os.listdir(subDirPath):
                eachFilePath = os.path.join(subDirPath, eachFile)
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
                            
                            regex = re.compile("^[a-z]+$")
                            if regex.match(blankWord):                #English word
                                word = word + blankWord + " "
                        #for blankWord
                        
                        abstract = abstract + word + " "
                    #for word
                #for line
                outFilePath = os.path.join(outSubDirPath, conference + subDir + str(num) + ".txt")
                outFileHandler = open(outFilePath, "w")
                outFileHandler.write(abstract)
                outFileHandler.close()
                print(num)
                num = num + 1
            #for eachFile
    #def
#class
conference = "icdt"
rootDir = r"C:\Users\dcsliub\Desktop\HierarchyData\abstactdata" + "\\" + conference
textDirName = "text"
abstractDirName = "abstract"
textDir = os.path.join(rootDir, textDirName)
abstractDir = os.path.join(rootDir, abstractDirName)
nipsExtractor = TextExtractor()
yearList = ["14"]
nipsExtractor.extractFromText(textDir, abstractDir, conference, yearList)
print("Program ends")