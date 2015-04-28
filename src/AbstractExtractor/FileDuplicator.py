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
conference = "mm"
#yearList = ["14"]
yearList = ["14", "13", "12", "11", "10", "09"]
rootDir = r'C:\Users\dcsliub\Desktop\abstactdata' +'\\' + conference 

abstractDir = "abstract"

for year in yearList:
    inDir = os.path.join(rootDir, abstractDir, year)
    outDir = os.path.join(rootDir, conference)
    if not os.path.exists(outDir):
        os.mkdir(outDir)
    
    fileDuplicator.duplicateFile(inDir, outDir)
#for
print("Program ends")