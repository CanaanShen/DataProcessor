'''
Created on Apr 27, 2015

@author: dcsliub

'''
import os

class CVPRExtractor:
    
    def __init__(self):
        self.punctuation = [".", ",", ")", "(", "?", ":", "'", "\"", ";"]
        self.dgwList = ["eg", "et", "al", "etc"]
    
    def extractCVPR(self, textDir, abstractDir, year, conference):
        
        punctuation = [".", ",", ")", "(", "?", ":", "'", "\""]
        dgwList = ["eg", "et", "al", "etc"]
        
        inSubDirPath = os.path.join(textDir, year)
        outSubDirPath = os.path.join(abstractDir, year)
        if not os.path.exists(outSubDirPath):
            os.mkdir(outSubDirPath)
            
        num = 0
        for eachFile in os.listdir(inSubDirPath):
            eachFilePath = os.path.join(inSubDirPath, eachFile)
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
                            if subWord.isalpha():
                                word = word + subWord + " "
                     
                    if (" " not in word) and (not word.isalpha()):                #English word
                        continue;
                            
                    for dgw in dgwList:                   #DGW
                        if word == dgw:
                            word = ""
                            break;
                        
                    abstract = abstract + word + " "
                #for
            #for
            outFilePath = os.path.join(outSubDirPath, conference + year + str(num) + ".txt")
            outFileHandler = open(outFilePath, "w")
            outFileHandler.write(abstract)
            outFileHandler.close()
            print(num)
            num = num + 1
        #for  
    #def
    
    def extractCVPR_Text(self, textDir, abstractDir, year, conference):
        
        inFile = os.path.join(textDir, year, conference+year+".txt")
        outSubDirPath = os.path.join(abstractDir, year)
        if not os.path.exists(outSubDirPath):
            os.mkdir(outSubDirPath)
        
        inFileHandler = open(inFile, "r")
        content = inFileHandler.readlines()
        
        num = 0
        for line in content:

            words = line.strip("\n").strip().lower().split()
            if len(words) < 15:    #title or author
                continue
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
                            word = word + subWord +" "
                     
                if (" " not in word) and (not word.isalpha()):                #English word
                    continue;
                
                for dgw in self.dgwList:                   #DGW
                    if word == dgw:
                        word = ""
                        break;
                
                abstract = abstract + word + " "
            #for
            
            outFile = os.path.join(outSubDirPath, conference+year+str(num)+".txt")
            outFileHandler = open(outFile, "w")
            outFileHandler.write(abstract)
            outFileHandler.close()
            num = num + 1
            print(num)
        #for
#class

conference = "sigir"
rootDir = r"C:\Users\dcsliub\Desktop\abstactdata" + "\\" + conference
textDirName = "text"
abstractDirName = "abstract"
year = "14"
textDir = os.path.join(rootDir, textDirName)
abstractDir = os.path.join(rootDir, abstractDirName)
conference = "sigir"
cvprExtractor = CVPRExtractor()
cvprExtractor.extractCVPR_Text(textDir, abstractDir, year, conference)
print("Program ends")