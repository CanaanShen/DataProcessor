'''
Created on Apr 30, 2015

@author: dcsliub
'''

import os

class DocumentFrequencyStat(object):
    
    def __init__(self):
        '''
        Constructor
        '''
        self.threshold = 1
    #def
    
    def statDocumentFrequency(self, subDirPath, conference):
        '''
        '''
        textDirPath = os.path.join(subDirPath, conference)
        print(textDirPath)
        
        docFreqMap = {}
        for file in os.listdir(textDirPath):
            fileNum = file.replace(".txt", "")
            filePath = os.path.join(textDirPath, file)
            fileHandler = open(filePath, "r")
            lines = fileHandler.readlines()
            for line in lines:
                words = line.strip("\n").strip().split()
                lineList = []
                for word in words:
                    if word not in lineList:       #only one time
                        lineList.append(word)
                #for word
                for word in lineList:
                    docList = []
                    if word in docFreqMap:
                        docList = docFreqMap[word]
                        docList.append(fileNum)
                        docFreqMap[word] = docList
                    else:
                        docList.append(fileNum)
                        docFreqMap[word] = docList
                    #if word
                #for word 
            #for line
        #for file
        
        reservedWordList = []
        reservedDocFreqMap = {}
        for word in docFreqMap:
            docList = docFreqMap[word]
            if len(docList) > self.threshold:
                reservedDocFreqMap[word] = docList
                reservedWordList.append(word)
        #for word
        
        outFile = os.path.join(subDirPath, conference + ".docfreqy")  #output docfreqy
        outFileHandler = open(outFile, "w")
        for key in reservedDocFreqMap:
            outFileHandler.write(key + ":")
            docList = reservedDocFreqMap[key]
            for doc in docList:
                outFileHandler.write(doc + " ")
            outFileHandler.write("\n")
        outFileHandler.close()
        
        outFile = os.path.join(subDirPath, conference + ".vocab")  #output vocab
        outFileHandler =  open(outFile, "w")
        for key in reservedDocFreqMap:
            outFileHandler.write(key + "\n")
        #for
        
        newDir = os.path.join(subDirPath, conference+ "_new")
        if not os.path.exists(newDir):
            os.mkdir(newDir)
        
        for file in os.listdir(textDirPath):
            inFilePath = os.path.join(textDirPath, file)
            outFilePath = os.path.join(newDir, file)
            inFileHandler = open(inFilePath, "r")
            outFileHandler = open(outFilePath, "w")
            lines = inFileHandler.readlines()
            
            newLine = ""
            for line in lines:
                words = line.strip("\n").strip().split()
                for word in words:
                    if word in reservedWordList:
                        newLine = newLine + word + " " 
                #for word
            #for line
            outFileHandler.write(newLine)
        #for file
    #def
        
    def main(self):
        rootDir = r"C:\Users\dcsliub\Desktop\HierarchyData\abstactdata"
        for conference in os.listdir(rootDir):
            subDirPath = os.path.join(rootDir, conference)
            self.statDocumentFrequency(subDirPath, conference)
    #def
#class

if __name__ == "__main__":
    documentStat = DocumentFrequencyStat()
    documentStat.main()
    print("Program ends")

#         wholeVocab = len(docFreqMap)
#         sortedTupleList = sorted(docFreqMap.items(), key=lambda d:d[1], reverse = True)
#         outFile = os.path.join(subDirPath, conference + ".olddocfreq")
#         print(outFile)
#         outFileHandler = open(outFile, "w")
#         for element in sortedTupleList:
#             outFileHandler.write(element[0] + ":" + str(element[1]) + "\n")
#         outFileHandler.close()
#         amount = wholeVocab * 

#         outFile = os.path.join(subDirPath, conference + ".olddocfreq")
#         outFileHandler = open(outFile, "w")
#         for key in docFreqMap:
#             outFileHandler.write(key + ":")
#             docList = docFreqMap[key]
#             for doc in docList:
#                 outFileHandler.write(doc + " ")
#             outFileHandler.write("\n")
#         outFileHandler.close()
        