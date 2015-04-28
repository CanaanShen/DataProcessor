'''
Created on Apr 27, 2015

@author: dcsliub

'''
import os

class JMLRExtractor:
    
    def __init__(self):
        self.punctuation = [".", ",", ")", "(", "?", ":", "'", "\"", ";"]
        self.dgwList = ["eg", "et", "al", "etc"]
        
    def extractJMLR(self, textDir, abstractDir, conference):
        
        for subDir in os.listdir(textDir):
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
                        
                        for punct in self.punctuation:
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
                            
                        for dgw in self.dgwList:                   #DGW
                            if word == dgw:
                                word = ""
                                break;
                        
                        abstract = abstract + word + " "
                    #for
                #for
                outFilePath = os.path.join(outSubDirPath, conference + subDir + str(num) + ".txt")
                outFileHandler = open(outFilePath, "w")
                outFileHandler.write(abstract)
                outFileHandler.close()
                print(num)
                num = num + 1
            #for
    #def
#class

conference = "jmlr"
rootDir = "C:\\Users\\dcsliub\\Desktop\\abstactdata\\" + conference
textDirName = "text"
abstractDirName = "abstract"
textDir = os.path.join(rootDir, textDirName)
abstractDir = os.path.join(rootDir, abstractDirName)
conference = "jmlr"
jmlrExtractor = JMLRExtractor()
jmlrExtractor.extractJMLR(textDir, abstractDir, conference)
print("Program ends")