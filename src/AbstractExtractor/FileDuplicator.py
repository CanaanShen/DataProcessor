'''
Created on Apr 28, 2015

@author: dcsliub
'''
import os

class FileDuplicator:
    def duplicateFile(self, inDir, outDir):
        
        for file in os.listdir(inDir):
            inFile = os.path.join(inDir, file)
            outFile = os.path.join(outDir, file)
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
            else:
                print(inFile)
        
    #def
#class

fileDuplicator = FileDuplicator()
abstractDir = "abstract"

rootDir = r'C:\Users\dcsliub\Desktop\HierarchyData\abstactdata' 

for conference in os.listdir(rootDir):
    
    conferenceDir = os.path.join(rootDir, conference)
    
    inDir = os.path.join(conferenceDir, abstractDir)
    outDir = os.path.join(conferenceDir, conference)
    if not os.path.exists(outDir):
        os.mkdir(outDir)
    for subDir in os.listdir(inDir):
        subDirPath = os.path.join(inDir, subDir)
        print(subDirPath)
        fileDuplicator.duplicateFile(subDirPath, outDir)
    #for year
#for conference
print("Program ends")