'''
Created on Apr 27, 2015

@author: dcsliub
'''

import os

class ACLExtractor:
    def extractACL(self, textDir, abstractDir, year, prefix):
        punctuation = [".", ",", ")", "(", "?", ":", "-"]
        dgwList = ["eg", "et", "al", "etc"]
        
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
                        
                    for punct in punctuation:
                        if punct in word:
                            word = word.replace(punct, "")
                    #for
                        
                    if not word.isalpha():                #English word
                        continue;
                    
                    for dgw in dgwList:                   #DGW
                        if word == dgw:
                            word = ""
                            break;
                    #for
                    
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
#class

conference = "acl"
year  = "13"
rootDir = r"C:\Users\dcsliub\Desktop\abstactdata" + "\\" + conference
textDirName = "text"
abstractDirName = "abstract"
textDir = os.path.join(rootDir, textDirName, year)
abstractDir = os.path.join(rootDir, abstractDirName, year)
prefix = "acl"
aclExtractor = ACLExtractor()
aclExtractor.extractACL(textDir, abstractDir, year, prefix)
print("Program ends")
