'''
Created on Apr 27, 2015

@author: dcsliub

'''
import os

class JMLRExtractor:
    
    def extractJMLR(self, textDir, abstractDir, prefix):
        
        punctuation = [".", ",", ")", "(", "?", ":", "-"]
        
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
                        
                        for punct in punctuation:
                            if punct in word:
                                word = word.replace(punct, "")
                        #for
                        
                        if not word.isalpha():                #English word
                            continue;
                        
                        abstract = abstract + word + " "
                    #for
                #for
                outFilePath = os.path.join(outSubDirPath, prefix + subDir + str(num) + ".txt")
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
prefix = "jmlr"
jmlrExtractor = JMLRExtractor()
jmlrExtractor.extractJMLR(textDir, abstractDir, prefix)
print("Program ends")