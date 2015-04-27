'''
Created on Apr 27, 2015

@author: dcsliub

'''
import os

class CVPRExtractor:
    
    def extractCVPR(self, textDir, abstractDir, year, prefix):
        
        punctuation = [".", ",", ")", "(", "?", ":", "-"]
        
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
                        
                    if not word.isalpha():                #English word
                        continue;
                        
                    abstract = abstract + word + " "
                #for
            #for
            outFilePath = os.path.join(outSubDirPath, prefix + year + str(num) + ".txt")
            outFileHandler = open(outFilePath, "w")
            outFileHandler.write(abstract)
            outFileHandler.close()
            print(num)
            num = num + 1
        #for  
    #def
    
    def extractCVPR_Text(self, textDir, abstractDir, year, prefix):
        
        punctuation = [".", ",", ")", "(", "?", ":", "-"]
        
        inFile = os.path.join(textDir, year, prefix+year+".txt")
        outSubDirPath = os.path.join(abstractDir, year)
        if not os.path.exists(outSubDirPath):
            os.mkdir(outSubDirPath)
        
        inFileHandler = open(inFile, "r")
        content = inFileHandler.readlines()
        
        num = 0
        for line in content:
            abstract = ""
            words = line.strip("\n").strip().lower().split()
            if len(words) < 15:    #title or author
                continue
            
            for word in words:
                for punct in punctuation:
                    if punct in word:
                        word = word.replace(punct, "")
                #for
                        
                if not word.isalpha():                #English word
                    continue;
                        
                abstract = abstract + word + " "
            #for
            
            outFile = os.path.join(outSubDirPath, prefix+year+str(num)+".txt")
            outFileHandler = open(outFile, "w")
            outFileHandler.write(abstract)
            outFileHandler.close()
            num = num + 1
        #for
#class

conference = "cvpr"
rootDir = "C:\\Users\\dcsliub\\Desktop\\abstactdata\\" + conference
textDirName = "text"
abstractDirName = "abstract"
year = "11"
textDir = os.path.join(rootDir, textDirName)
abstractDir = os.path.join(rootDir, abstractDirName)
prefix = "cvpr"
cvprExtractor = CVPRExtractor()
cvprExtractor.extractCVPR_Text(textDir, abstractDir, year, prefix)
print("Program ends")