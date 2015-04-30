'''
Created on Apr 20, 2015

@author: dcsliub
'''

import os

class MalletDataProcessor:
    
    def lineAsDoc(self, rootDir):
        
        for dir in os.listdir(rootDir):
            docFile = os.path.join(rootDir, dir, dir+".docs")
            vocabFile = os.path.join(rootDir, dir, dir+".vocab")
            
            docFileHandler = open(docFile, "r")
            vocabFileHandler = open(vocabFile, "r")
            
            vocabMap = {}
            line = " "
            while len(line) != 0:
                line = vocabFileHandler.readline().strip("\n").strip()
                
                if len(line) == 0:
                    continue
                
                vocabIDWord = []
                vocabIDWord = line.split(":")
                if len(vocabIDWord) != 2:
                    print("vocabIDWord size error")
                    return
                
                vocabID = int(vocabIDWord[0])
                vocabStr = vocabIDWord[1]
                vocabMap[vocabID] = vocabStr
            #while
            
            line = " "
            lineNum = 0
            while True:
                line = docFileHandler.readline()
                
                if line == "":  #the end of a file
                    break
                
                line = line.strip("\n").strip()
      
                if len(line) == 0:   #blank
                    continue
                
                wordIDList = []
                wordIDList = line.split(" ")
                if len(wordIDList) == 0:
                    print("docIDList size error")
                    return
                
                lineDocFile = os.path.join(rootDir, dir, str(lineNum) + ".txt")
                lineDocFileHandler = open(lineDocFile, "w")
                lineDoc = ""
                for wordID in wordIDList:
                    intWordID = int(wordID)
                    
                    wordStr=""
                    if intWordID in vocabMap.keys():
                        wordStr = vocabMap[intWordID]
                    else:
                        print(str(intWordID) + "does not exist")
                    lineDoc = lineDoc + wordStr + " "
                #for
                lineDocFileHandler.write(lineDoc)
                lineDocFileHandler.close()
                lineNum = lineNum + 1
    #def
    
    #document --> document
    def documentAsDocument(self, rootDir):
        
        for dir in os.listdir(rootDir):
            docFile = os.path.join(rootDir, dir, dir+".docs")
            vocabFile = os.path.join(rootDir)
    #def
#class

dataProcessor = MalletDataProcessor()
#rootDir = "..\mallet"
rootDir = "..\DocumentasDocument"
#dataProcessor.documentAsDocument(rootDir)
dataProcessor.lineAsDoc(rootDir)
print("Program ends")