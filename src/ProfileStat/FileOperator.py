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
            
def removeAllFile(dir):
    for eachFile in os.listdir(dir):
        filePath = os.path.join(dir, eachFile)
        os.remove(filePath)

def deleteDir(dir, conference):
    
    targetDir = os.path.join(dir, conference+"_old")
    shutil.rmtree(targetDir)

def copyFile(file, sourceDir, targetDir):
    sourceFile = os.path.join(sourceDir, file)
    #targetFile = os.path.join(targetDir, file)
    shutil.copy(sourceFile, targetDir)

def copyFiles_2(sourceDir, targetDir):
    print(targetDir)
    if not os.path.exists(targetDir):
        os.mkdir(targetDir)
        
    for file in os.listdir(sourceDir):
        filePath = os.path.join(sourceDir, file)
        shutil.copy(filePath, targetDir)

def copyFiles(prefix, suffixList, sourceDir, targetDir):
    
    if not os.path.exists(targetDir):
        os.mkdir(targetDir)
    
    for suffix in suffixList:
        file = os.path.join(sourceDir, prefix + suffix)
        targetFile = os.path.join(targetDir, prefix + suffix)
        if os.path.exists(targetFile):
            os.remove(targetFile)
        
        if os.path.exists(file):
            shutil.copy(file, targetDir)
        else:
            print(file, "does not exist")
    #for
#def

def copyFile_3(dirPath, conference, suffix):
    inFilePath = os.path.join(dirPath, conference, conference + suffix + ".freqy")
    outFilePath = os.path.join(dirPath, conference, conference + suffix + ".knowl")
    shutil.copy(inFilePath, outFilePath)
#def

def generateEmptyFiles(dirPath, suffix, number):
    for i in range( number):
        filePath = os.path.join(dirPath, str(i)+suffix)
        fileHandler = open(filePath, "w");
        fileHandler.close;
#def

def copyFilesintoOneFolder(sourceDirPath, targetDirPath):
    
    targetFiles = os.listdir(targetDirPath)
    targetFileNum = len(targetFiles)

    for file in os.listdir(sourceDirPath):
        sourceFilePath = os.path.join(sourceDirPath, file)
        targetFilePath = os.path.join(targetDirPath, str(targetFileNum) + ".txt");
        shutil.copyfile(sourceFilePath, targetFilePath)
        targetFileNum = targetFileNum + 1;
        
#def
    
if __name__ == "__main__":
    
#     rootDir = r"C:\Users\Yueshen\workspace_luna\Mallet\file\output\Conference_HierarchicalPAM"
#     for conference in os.listdir(rootDir):
#         dirPath = os.path.join(rootDir, conference)
# #         removeAllFile(dirPath)
    
    sourceRootDirPath = r"C:\Users\dcsliub\Desktop\data"
    targetRootDirPath = r"C:\Users\Yueshen\workspace_luna\Mallet\file\input\Conference"
    for conference in os.listdir(sourceRootDirPath):
        sourceDirPath = os.path.join(sourceRootDirPath, conference)
        targetDirPath = os.path.join(targetRootDirPath, conference)
        suffixList = [".wordfreqy"]
        copyFiles(conference, suffixList, sourceDirPath, targetDirPath)

#         if conference == targetDir:     #itself
#             continue
#         
#         sourceDirPath = os.path.join(sourceRootDirPath, conference, conference);
#         targetDirPath = os.path.join(targetRootDirPath, targetDir)
#         copyFilesintoOneFolder(sourceDirPath, targetDirPath)
    
#     suffixList = {".mallet", ".docstat", ".vocab", ".docfreqyptry", ".docfreqy"}
#     sourceRootDir = r"C:\Users\dcsliub\Desktop\data"
#     targetRootDir = r"C:\Users\Yueshen\workspace_luna\Mallet\file\input\Conference"
#     for conference in os.listdir(sourceRootDir):
#         sourceDir = os.path.join(sourceRootDir, conference)
#         targetDir = os.path.join(targetRootDir, conference)
#         copyFiles(conference, suffixList, sourceDir, targetDir)
#     suffixList = {".mallet", ".docstat"}
#     for dir in os.listdir(sourceRootDir):
#         removeFileBasedonFormat(os.path.join(sourceRootDir, dir), dir, suffixList)
#     suffixList = {".mallet", ".olddocfreq", ".oldvocab"}
#     rootDir = r"C:\Users\dcsliub\Desktop\HierarchyData\abstactdata"
#     for conference in os.listdir(rootDir):
#         subDirPath = os.path.join(rootDir, conference)
#         removeFileBasedonFormat(subDirPath, conference, suffixList)
    
#     suffixList = [".tree", ".topiccoherence"]
#     sourceRootDir = r"C:\Users\dcsliub\Desktop\Conference"
#     targetRootDir = r"C:\Users\Yueshen\workspace_luna\Mallet\file\output\Conference\Iteration0"
#     for conference in os.listdir(targetRootDir):
#         sourceDir = os.path.join(sourceRootDir, conference)
#         targetDir = os.path.join(targetRootDir, conference)
#         conference = conference + "_2500_3_30"
#         copyFiles(conference, suffixList, sourceDir, targetDir)
#         targetDir = os.path.join(targetRootDir, conference)
#         prefix = conference
#         copyFiles(prefix, suffixList, sourceDir, targetDir)
#     confereneList = ["ecml", "icdt", "edbt", "sac", "ideas", "wi"]
#     for conference in confereneList:
#         sourceDir = os.path.join(sourceRootDir, conference)
#         targetDir = os.path.join(targetRootDir, conference)

    print("Program ends")