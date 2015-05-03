'''
Created on May 1, 2015

@author: dcsliub
'''
import os
import shutil

def removeFileBasedonFormat(dir, prefix, suffixList):
    for suffix in suffixList:
        file = os.path.join(dir, prefix + suffix)
        if os.path.exists(file):
            os.remove(file)
            
def copyFile(file, sourceDir, targetDir):
    sourceFile = os.path.join(sourceDir, file)
    #targetFile = os.path.join(targetDir, file)
    shutil.copy(sourceFile, targetDir)

def copyFiles(prefix, suffixList, sourceDir, targetDir):
    for suffix in suffixList:
        file = os.path.join(sourceDir, prefix + suffix)
        if os.path.exists(file):
            shutil.copy(file, targetDir)
        else:
            print(file, "does not exist")
    #for

if __name__ == "__main__":
    
#     suffixList = {".mallet", ".olddocfreq", ".oldvocab"}
#     rootDir = r"C:\Users\dcsliub\Desktop\HierarchyData\abstactdata"
#     for conference in os.listdir(rootDir):
#         subDirPath = os.path.join(rootDir, conference)
#         removeFileBasedonFormat(subDirPath, conference, suffixList)
    
    suffixList = [".vocab", ".docfreqy"]
    sourceRootDir = r"C:\Users\dcsliub\Desktop\HierarchyData\abstactdata"
    targetRootDir = r"C:\Users\Yueshen\workspace_luna\Mallet\file\input\Conference"
    for conference in os.listdir(sourceRootDir):
        sourceDir = os.path.join(sourceRootDir, conference)
        targetDir = os.path.join(targetRootDir, conference)
        copyFiles(conference, suffixList, sourceDir, targetDir)
    print("Program ends")