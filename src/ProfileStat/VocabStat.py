'''
Created on Apr 30, 2015

@author: dcsliub
'''
import os

class VocabStat(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    #def
    
    def statVocab(self, inputDir, outputDir, conference):
        '''
        statVocab
        '''
        vocabList = []
        
        for file in os.listdir(inputDir):
            filePath = os.path.join(inputDir, file)
            fileHandler = open(filePath, "r")
            lines = fileHandler.readlines()
            
            for line in lines:
                words = line.strip("\n").strip().split()
                for word in words:
                    if not word in vocabList:
                        vocabList.append(word)
                #for
            #for line
        #for file
        vocabFile = os.path.join(outputDir, conference+".oldvocab")
        vocabFileHandler = open(vocabFile, "w")
        for word in vocabList:
            vocabFileHandler.write(word + "\n")
        #for
        vocabFileHandler.close()
    #def
    
    def main(self):
        rootDir = r"C:\Users\dcsliub\Desktop\HierarchyData\abstactdata"
        for dir in os.listdir(rootDir):
            subDirPath = os.path.join(rootDir, dir)
            textDirPath = os.path.join(subDirPath, dir)
            print(textDirPath)
            self.statVocab(textDirPath, subDirPath, dir)
            print(dir)
#class
vocabStat = VocabStat()
vocabStat.main()
print("Program ends")