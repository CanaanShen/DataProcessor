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
#class

fileDuplicator = FileDuplicator()
abstractDir = "abstract"

rootDir = r'C:\Users\dcsliub\Desktop\HierarchyData\abstactdata' 

conferenceList = []

for conference in os.listdir(rootDir):
    
    conferenceDir = os.path.join(rootDir, conference)
    
    inDirPath = os.path.join(conferenceDir, abstractDir)
    outDirPath = os.path.join(conferenceDir, conference)
    print(outDirPath)
    if os.path.exists(outDirPath):
        for file in os.listdir(outDirPath):
            os.remove(os.path.join(outDirPath, file))

    fileDuplicator.duplicateFile(inDirPath, outDirPath)
    #for year
#for conference
print("Program ends")