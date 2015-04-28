'''
Created on Apr 21, 2015

@author: dcsliub
'''
import os

class NIPSDataProcessor:
    
    def extractNIPSAbstract(self, rootDir, outputDir):
        
        punctuation = [".", ",", ")", "(", "?", ":"]
        
        for subDir in os.listdir(rootDir):
            subDirPath = os.path.join(rootDir, subDir)
            
            subOutputDirPath = os.path.join(outputDir, subDir)
            if not os.path.exists(subOutputDirPath):
                os.mkdir(subOutputDirPath)
            
            for eachFile in os.listdir(subDirPath):
                eachFilePath = os.path.join(subDirPath, eachFile)
                eachFileHandler = open(eachFilePath, "r")
                
                eachOutputFilePath = os.path.join(subOutputDirPath, subDir + eachFile)
                print(eachOutputFilePath)
                abstract = ""
                line = ""
                beginMark = 0
                mark = 0
                doc = ""
                conference = ""
                while True:
                    line = eachFileHandler.readline()
                    
                    if len(line) == 0:
                        continue;
                    
                    line = line.lower()
                    
                    if ("abstract" in line) and (mark == 0):
                        beginMark = 1
                        mark = 1
                        continue
                    
                    if "introduction" in line:
                        break
                    
                    if beginMark > 13:   #no "introduction"
                        break;
                    
                    if beginMark >= 1:              #abstract
                        line = line.strip("\n").strip()
                        lineList = []
                        lineList = line.split(" ")

                        newLine = ""
                        
                        index = -1
                        for word in lineList:
                            index = index + 1   #the next one
                            
                            if index == 0: #the first word
                                word = conference + word
                                conference = ""
                            
                            for punct in punctuation:
                                if punct in word:
                                    word = word.replace(punct, "")
                            
                            if index < (len(lineList) - 1):
                                if not word.isalpha():                #English word
                                    continue;
                            
                            if index < (len(lineList)-1):            
                                newLine = newLine + word + " "
                            else:
                                
                                if "-" in word:
                                    word = word.replace("-", "")
                                    conference = word
                                else:
                                    newLine = newLine + word + " "
                        #for\
                        beginMark = beginMark + 1
                        doc = doc + newLine + " "
                    #if
                #while
                
                eachoutputFileHanlder = open(eachOutputFilePath, "w")
                eachoutputFileHanlder.write(doc + "\n")
                eachoutputFileHanlder.close()
                
        #for
    #def  
#class

nipsDataProcessor = NIPSDataProcessor()
rootDir = "..\\nipstxt"
outputDir = "..\\nipsabstract"
nipsDataProcessor.extractNIPSAbstract(rootDir, outputDir)
print("Program ends")