'''
Created on Apr 27, 2015

@author: dcsliub
'''
'''
Created on Apr 26, 2015

@author: dcsliub
'''
import os

class IJCAIExtractor:
    
    def __init__(self):
        self.punctuation = [".", ",", ")", "(", "?", ":", "'", "\""]
        self.dgwList = ["eg", "et", "al", "etc"]
    
    def extractIJCAI(self, textDir, abstractDir, year, conference):
                
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
    
    def extractIJCAI_Text(self, textDir, abstractDir, year, conference):
        

        
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
                        word = word + " " + subWord
                     
                if (" " not in word) and (not word.isalpha()):                #English word
                    continue;
                            
                for dgw in self.dgwList:                   #DGW
                    if word == dgw:
                        word = ""
                        break;
                        
                abstract = abstract + word + " "
            #for word
            
            outFile = os.path.join(outSubDirPath, conference+year+str(num)+".txt")
            outFileHandler = open(outFile, "w")
            outFileHandler.write(abstract)
            outFileHandler.close()
            num = num + 1
            print(num)
        #for
#class

rootDir = "C:\\Users\\dcsliub\\Desktop\\abstactdata\\ijcai"
textDirName = "text"
abstractDirName = "abstract"
year = "13"
textDir = os.path.join(rootDir, textDirName)
abstractDir = os.path.join(rootDir, abstractDirName)
conference = "ijcai"
ijcaiExtractor = IJCAIExtractor()
ijcaiExtractor.extractIJCAI(textDir, abstractDir, year, conference)
print("Program ends")