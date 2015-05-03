'''
Created on May 3, 2015
Vocab Difference
@author: dcsliub
'''
import os

def compareDiff(inFile, outFile, diffFile):
    inFileHandler = open(inFile, "r")
    outFileHandler = open(outFile, "r")
    diffFileHandler = open(diffFile, "w")
    
    inVocabList = []
    outVocabList = []
    diffVocabList = []
    lines = inFileHandler.readlines()
    for line in lines:
        line = line.strip("\n").strip()
        inVocabList.append(line)
    #for
    
    lines = outFileHandler.readlines()
    for line in lines:
        line = line.strip("\n").strip()
        outVocabList.append(line)
    #for
    
    for word in inVocabList:
        if not word in outVocabList:
            diffVocabList.append("vocab: " + word)
    #for
    
    for word in outVocabList:
        if not word in inVocabList:
            diffVocabList.append("alphabet: " + word)
    
    for word in diffVocabList:
        diffFileHandler.write(word + "\n")
    #for
    
    inFileHandler.close()
    outFileHandler.close()
    diffFileHandler.close()
#def

if __name__ == "__main__":
    
    inSuffix = ".vocab"
    outSuffix = ".alphabet"
    inRootDir = r"C:\Users\Yueshen\workspace_luna\Mallet\file\input\Conference"
    outRootDir = r"C:\Users\Yueshen\workspace_luna\Mallet\file\output\Conference"
    for conference in os.listdir(inRootDir):
        inFile = os.path.join(inRootDir, conference, conference + inSuffix)
        outFile = os.path.join(outRootDir, conference, conference + outSuffix)
        diffFile = os.path.join(outRootDir, conference, conference + ".vocabdiff")
        compareDiff(inFile, outFile, diffFile)
    print("Program ends")
#if