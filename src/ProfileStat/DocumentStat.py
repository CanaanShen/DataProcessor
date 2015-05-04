'''
Created on May 4, 2015

@author: dcsliub
'''

import os

def statAverageDocLength(subDirPath, conference):
    subSubDirPath = os.path.join(subDirPath, conference)
    totalLength = 0
    files = os.listdir(subSubDirPath)
    for file in files:
        filePath = os.path.join(subSubDirPath, file)
        fileHandler = open(filePath, "r")
        content = fileHandler.read().strip("\n").strip()
        words = content.split()
        totalLength = totalLength + len(words)
    #for
    docSize = len(files)
    averageDocLen = float(totalLength)/float(docSize)
    
    return averageDocLen
#def        

def statDocument(subDirPath, conference):
    averageDocLen = statAverageDocLength(subDirPath, conference)
    outFile = os.path.join(subDirPath, conference+".docstat")
    outFileHandler = open(outFile, "w")
    outFileHandler.write(str(averageDocLen))
    outFileHandler.close()
#def

if __name__ == '__main__':
    rootDir = r"C:\Users\dcsliub\Desktop\HierarchyData\abstactdata"
    for conference in os.listdir(rootDir):
        subDirPath = os.path.join(rootDir, conference)
        statDocument(subDirPath, conference)
    #for 
    print("Program ends")