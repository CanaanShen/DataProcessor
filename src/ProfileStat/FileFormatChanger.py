'''
Created on May 4, 2015

@author: dcsliub
'''
import os

def changeFileFormat(filePath):
    
    if not os.path.exists(filePath):
        print("file does not exist")
        return
    
    fileHandler = open(filePath, "r")
    lines = fileHandler.readlines()
    
    newLines = []
    blank_1 = "   "
    blank_2 = "      "
    blank_3 = "         "
    for line in lines:
        num = 2
        if blank_3 in line:
            num = 3
        elif blank_2 in line:
            num = 2
        elif blank_1 in line:
            num = 1
        else:
            num = 0
        
        line = line.strip("\n").strip()
        line  = str(num) + "-" + line
        prefix = ""
        for i in range(num):
            prefix = prefix + blank_1
        line = prefix + line
        newLines.append(line)
    #for
    
    fileHandler.close()
    fileHandler = open(filePath, "w")
    for line in newLines:
        fileHandler.write(line + "\n")
    fileHandler.close()
#def


if __name__ == "__main__":
    
    rootDir = r"C:\Users\Yueshen\workspace_luna\Mallet\file\output\Conference"
    reversedConferenceList = ["ecml", "icdt", "edbt", "sac", "ideas", "wi"]
    for conference in os.listdir(rootDir):
        if conference not in reversedConferenceList:
            targetDir = os.path.join(rootDir, conference)
            numIteration = str(5000)
            layer = str(3)
            numWordsToDisplay = str(30)
            suffix = "_" + numIteration + "_" + layer + "_" + numWordsToDisplay + '.tree'
            
            filePath = os.path.join(targetDir, conference + suffix)
            print(filePath)
            changeFileFormat(filePath)

    #for conference
    print("Program ends")