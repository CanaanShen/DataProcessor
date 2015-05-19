'''
Created on May 4, 2015

@author: dcsliub
'''

import os
from src.AbstractExtractor.AAAIExtractor import conference

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

def statDocSize(subDirPath, conference):
    subSubDirPath = os.path.join(subDirPath, conference)
    docSize = os.listdir(subSubDirPath)
    return len(docSize)

def statDocument(subDirPath, conference):
    blank = "   " 
    
    averageDocLen = statAverageDocLength(subDirPath, conference)
    averageDocLen = float("{0:0.4f}".format(averageDocLen))
    docSize = statDocSize(subDirPath, conference)
    
    outFile = os.path.join(subDirPath, conference+".docstat")
    outFileHandler = open(outFile, "w")
    outFileHandler.write("<DocStat>" + "\n")
    outFileHandler.write(blank + "<Avglen>" + str(averageDocLen) + "</Avglen>" + "\n")
    outFileHandler.write(blank + "<Docnum>" + str(docSize) + "</Docnum>" + "\n")
    outFileHandler.write("</DocStat>")
    outFileHandler.close()
#def


if __name__ == '__main__':
    rootDir = r"C:\Users\dcsliub\Desktop\data"
#     conferenceList = ['ecml', 'edbt', "icdt", 'ideas', 'wi', 'wsdm']
    conferenceList = ["combinedtogether"]
    for conference in os.listdir(rootDir):
        subDirPath = os.path.join(rootDir, conference)
#         cmd = "cd.." + "\n" + "cd " + conference + "\n" + "mallet import-dir --input " + conference + " --output " + conference + ".mallet --keep-sequence \n" 
        cmd = "del C:\Users\Yueshen\workspace_luna\Mallet\file\output\Conference_HierarchicalPAM\\" + conference + "\\" + conference + "_*.*"
        print(cmd)
#         statDocument(subDirPath, conference)
    #for 
    print("Program ends")