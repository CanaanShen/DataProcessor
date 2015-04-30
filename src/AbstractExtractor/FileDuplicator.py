'''
Created on Apr 28, 2015

@author: dcsliub
'''
import os
import shutil

class FileDuplicator:
    def duplicateFile(self, inDir, outDir):
        
        for file in os.listdir(inDir):
            inFile = os.path.join(inDir, file)
            outFile = os.path.join(outDir, file)
            statInfo = os.stat(inFile)
            if not statInfo.st_size == 0:
                shutil.copyfile(inFile, outFile)
            else:
                print(inFile)
        
    #def
#class

fileDuplicator = FileDuplicator()
conference = "icdm"
conferenceList = ["iccv"]
#yearList = ["14"]
yearList = ["13", "11", "09", "07", "05", "03"]
abstractDir = "abstract"

for conference in conferenceList:
    rootDir = r'C:\Users\dcsliub\Desktop\abstactdata' +'\\' + conference 

    for year in yearList:
        inDir = os.path.join(rootDir, abstractDir, year)
        outDir = os.path.join(rootDir, conference)
        if not os.path.exists(outDir):
            os.mkdir(outDir)
    
        fileDuplicator.duplicateFile(inDir, outDir)
    #for year
#for
print("Program ends")