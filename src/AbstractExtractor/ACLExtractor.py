'''
Created on Apr 27, 2015

@author: dcsliub
'''

import os

class ACLExtractor:
    
    def __init__(self):
    
        self.punctuation = [".", ",", ")", "(", "?", ":", ";", "'", "\"", "-", "#", "$", "&", 
                       "^", "%", "*", "@", "`", "~", "/", "<", ">", "[", "]", "|", "=", "+", "_", "!"
                       "{", "}", "\\"]
        self.dgwList = ["e.g.", "et al", ".etc", "iii","ii", "i.e.", "(ie)", "(ie"]
    
    def extractACL(self, textDir, abstractDir, year, conference):

        
        outSubDirPath = os.path.join(abstractDir)
        if not os.path.exists(outSubDirPath):
            os.mkdir(outSubDirPath)
            
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
                    #for
                    
                    for punct in self.punctuation:
                        if punct in word:
                            word = word.replace(punct, " ")
                    #for
                        
                    blankWords = word.split()
                    word = ""
                    for blankWord in blankWords:
                        if blankWord != "k" and blankWord != "a" and blankWord != "x" and len(blankWord) == 1:
                            blankWord = ""
                            
                        if blankWord.isalpha():                #English word
                            word = word + blankWord + " "
                    #for
                    
                    abstract = abstract + word + " "
                #for word
            #for line
            outFilePath = os.path.join(outSubDirPath, conference + year + str(num) + ".txt")
            outFileHandler = open(outFilePath, "w")
            outFileHandler.write(abstract)
            outFileHandler.close()
            print(num)
            num = num + 1
        #for 
    #def
#class

conference = "acl"
yearList = ["14", "13"]
rootDir = r"C:\Users\dcsliub\Desktop\HierarchyData\abstactdata" + "\\" + conference
textDirName = "text"
abstractDirName = "abstract"
aclExtractor = ACLExtractor()

for year in yearList:
    textDir = os.path.join(rootDir, textDirName, year)
    abstractDir = os.path.join(rootDir, abstractDirName, year)
    aclExtractor.extractACL(textDir, abstractDir, year, conference)
#for year
print("Program ends")
