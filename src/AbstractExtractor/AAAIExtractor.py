'''
Created on Apr 26, 2015

@author: dcsliub
'''
import os

class AAAIExtractor:
    
    def __init__(self):
        self.punctuation = [".", ",", ")", "(", "?", ":", ";", "'", "\"", "-", "#", "$", "&", 
                       "^", "%", "*", "@", "`", "~", "/", "<", ">", "[", "]", "|", "=", "+", "_", "!"
                       "{", "}", "\\"]
        self.dgwList = ["e.g.", "et al", ".etc", "iii","ii", "i.e.", "(ie)", "(ie"]
    
    def extractAAAI(self, textDir, abstractDir, conference):
        
        
        for subDir in os.listdir(textDir):
            subDirPath = os.path.join(textDir, subDir)
            outSubDirPath = os.path.join(abstractDir, subDir)
            print(outSubDirPath)
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
                        #for blankWord
                        
                        abstract = abstract + word + " "
                    #for word
                #for line
                
                outFilePath = os.path.join(outSubDirPath, conference + subDir + str(num) + ".txt")
                outFileHandler = open(outFilePath, "w")
                outFileHandler.write(abstract)
                outFileHandler.close()
#                 print(num)
                num = num + 1
            #for eachFile
    #def
#class
rootDir = r"C:\Users\dcsliub\Desktop\HierarchyData\abstactdata\aaai"
textDirName = "text"
abstractDirName = "abstract"
textDir = os.path.join(rootDir, textDirName)
abstractDir = os.path.join(rootDir, abstractDirName)
conference = "aaai"
aaaiExtractor = AAAIExtractor()
aaaiExtractor.extractAAAI(textDir, abstractDir, conference)
print("Program ends")