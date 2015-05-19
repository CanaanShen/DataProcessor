'''
Created on Apr 28, 2015

@author: dcsliub
'''
import os

class FileDuplicator:
    
    def duplicateFile(self, inDirPath, outDirPath):
        
        num = 0
        for subDir in os.listdir(inDirPath):
            subDirPath = os.path.join(inDirPath, subDir)
            
            for file in os.listdir(subDirPath):
                inFile = os.path.join(subDirPath, file)
                outFile = os.path.join(outDirPath, str(num) + ".txt")
                statInfo = os.stat(inFile)
                if not statInfo.st_size == 0:
                    inFileHandler = open(inFile, "r")
                    lines = inFileHandler.readlines()
                
                    newLine = ""
                    for line in lines:
                        words = line.strip("\n").strip().split()
                        for word in words:
                            newLine = newLine + word + " "
                    #for line
                    outFileHandler = open(outFile, "w")
                    outFileHandler.write(newLine)
                    outFileHandler.close()
                    inFileHandler.close()
                    num = num + 1
                else:
                    print(inFile)
    #def
    
    def duplicateFile_2(self, inDirPath, outDirPath, yearList):
        
        files = os.listdir(outDirPath)
        fileNum = len(files)
        print(fileNum)

        for year in yearList:
             
            subDirPath = os.path.join(inDirPath, year)
             
            for file in os.listdir(subDirPath):
                inFile = os.path.join(subDirPath, file)
                outFile = os.path.join(outDirPath, str(fileNum) + ".txt")
                statInfo = os.stat(inFile)
                if not statInfo.st_size == 0:
                    inFileHandler = open(inFile, "r")
                    lines = inFileHandler.readlines()
                 
                    newLine = ""
                    for line in lines:
                        words = line.strip("\n").strip().split()
                        for word in words:
                            newLine = newLine + word + " "
                    #for line
                    outFileHandler = open(outFile, "w")
                    outFileHandler.write(newLine)
                    outFileHandler.close()
                    inFileHandler.close()
                    fileNum = fileNum + 1
                else:
                    print(inFile)
    #def    
    
#class

fileDuplicator = FileDuplicator()
abstractDir = "abstract"

rootDir = r'C:\Users\dcsliub\Desktop\HierarchyData\abstactdata' 

conferenceList = ["wsdm"]
yearList = {"08"}

for conference in conferenceList:
    
    conferenceDir = os.path.join(rootDir, conference)
    
    inDirPath = os.path.join(conferenceDir, abstractDir)
    outDirPath = os.path.join(conferenceDir, conference)
    
    print(outDirPath)
    if not os.path.exists(outDirPath):
        os.mkdir(outDirPath)

    fileDuplicator.duplicateFile_2(inDirPath, outDirPath, yearList)
    #for year
#for conference
print("Program ends")