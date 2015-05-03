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
        self.punctuation = [".", ",", ")", "(", "?", ":", ";", "'", "\"", "-", "#", "$", "&", 
                       "^", "%", "*", "@", "`", "~", "/", "<", ">", "[", "]", "|", "=", "+", "_", "!"
                       "{", "}", "\\"]
        self.dgwList = ["e.g.", "et al", ".etc", "iii","ii", "i.e.", "(ie)", "(ie"]
    
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
                        
                    abstract = abstract + word + " "
                #for word
            #for line
            outFilePath = os.path.join(outSubDirPath, conference + year + str(num) + ".txt")
            outFileHandler = open(outFilePath, "w")
            outFileHandler.write(abstract)
            outFileHandler.close()
            print(num)
            num = num + 1
        #for eachFile
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

                abstract = abstract + word + " "
            #for word
            
            outFile = os.path.join(outSubDirPath, conference+year+str(num)+".txt")
            outFileHandler = open(outFile, "w")
            outFileHandler.write(abstract)
            outFileHandler.close()
            num = num + 1
            print(num)
        #for line
#class

conference = "ijcai"
rootDir = r"C:\Users\dcsliub\Desktop\HierarchyData\abstactdata" + "\\" + conference
textDirName = "text"
abstractDirName = "abstract"
yearList = ["13", "11", "09", "07", "05", "03"]
textDir = os.path.join(rootDir, textDirName)
abstractDir = os.path.join(rootDir, abstractDirName)
ijcaiExtractor = IJCAIExtractor()

for year in yearList:
    if year == "13" or year == "11" or year == "09" or year == "07":
        ijcaiExtractor.extractIJCAI(textDir, abstractDir, year, conference)
    else:
        ijcaiExtractor.extractIJCAI_Text(textDir, abstractDir, year, conference)
#for
print("Program ends")