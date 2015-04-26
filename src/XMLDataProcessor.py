'''
Created on Apr 20, 2015

@author: dcsliub
'''

import os
import xml.dom.minidom

class XMLDataProcessor:
    
    def processXMLData(self, inputRootDir, outputRootDir):
        
        for dir in os.listdir(inputRootDir):
            totalNum = 1000
  
            for num in range(0, totalNum):
                docFile = os.path.join(inputRootDir, dir, dir + str(num) + ".txt")
                if not os.path.exists(docFile):
                    print(docFile + "does not exist")
                    continue
                #if
                try:
                    domTree = xml.dom.minidom.parse(docFile)
                except:
                    print(docFile)
                    
                collection =domTree.documentElement
                sentences = collection.getElementsByTagName("Sentence")
                
                docLemma = ""
                for sentence in sentences:
                    lemma = sentence.getElementsByTagName("Lemma")[0]
                    eachLemma = lemma.childNodes[0].data
                    
                    eachLemmaList = []
                    eachLemmaList = eachLemma.split(" ")
                    eachFilteredLemma=""
                    for eachWord in eachLemmaList:
                        
                        if eachWord.isalpha():            #only english words
                            eachFilteredLemma = eachFilteredLemma + eachWord + " "
                    #for
                    docLemma = docLemma + eachFilteredLemma
                #for
                dirList = []
                dirList = dir.split(" ")
                newDir = ""
                for element in dirList:
                    newDir = newDir+element
                
                outputDir = os.path.join(outputRootDir, newDir)
                if not os.path.exists(outputDir):
                    os.makedirs(outputDir)
                
                docLemmaFile = os.path.join(outputRootDir, newDir, str(num) + ".txt")
                outputFileHandler = open(docLemmaFile, "w")
                outputFileHandler.write(docLemma)
                outputFileHandler.close()
        #for
    
#def
    def generateNameList(self, rootDir):
        
        filePath = os.path.join(rootDir, "namelist.txt")
        fileHanlder = open(filePath, "w")
        for subDir in os.listdir(rootDir):
            dirPath = os.path.join(rootDir, subDir)
            if os.path.isdir(dirPath):
                content = "mallet import-dir --input " + subDir + " --output " + subDir + ".mallet --keep-sequence --remove-stopwords"
                fileHanlder.write(content + "\n")
            #if
        fileHanlder.close()
        #for
    #def
                

dataProcessor = XMLDataProcessor();
inputRootDir = "..\KDD2014-Electronics-50Domains(Original)"
#outputRootDir = "..\\KDD2014-Electronics-50Domains(File)"
outputRootDir = "..\\1000NewsDocumentasDocument(File)"
#dataProcessor.processXMLData(inputRootDir, outputRootDir)
dataProcessor.generateNameList(outputRootDir)
print("Program ends")