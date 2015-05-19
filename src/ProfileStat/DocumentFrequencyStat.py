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
        self.freqyThreshold = 0.40
    #def
    
    def statDocFreqyAndVocabbasedonThreshold(self, inDirPath, outDirPath, conference, stopWordPath):
        '''
        '''
        stopWordList = self.readList(stopWordPath)

        textInDirPath = os.path.join(inDirPath, conference)
        totalFileNum = len(os.listdir(textInDirPath))
        print(textInDirPath)
        
        textOutDirPath = os.path.join(outDirPath, conference);
        if os.path.exists(textOutDirPath):
            for file in os.listdir(textOutDirPath):
                filePath = os.path.join(textOutDirPath, file);
                os.remove(filePath);
        
        docFreqMap = {}
        for file in os.listdir(textInDirPath):
            fileNum = file.replace(".txt", "")
            filePath = os.path.join(textInDirPath, file)
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
        
        docFreqyPtryMap = {}
        for word in docFreqMap:
            docList = docFreqMap[word]
            freqy = len(docList)
            freqyPtry = freqy/totalFileNum
            docFreqyPtryMap[word] = freqyPtry
        #for word
    
        reservedWordList = []
        reservedDocFreqMap = {}
        reservedDocFreqyPtryMap = {}
        for word in docFreqMap:
            docList = docFreqMap[word]
            freqyPtry = docFreqyPtryMap[word]
            if len(docList) > self.threshold and freqyPtry < self.freqyThreshold and word not in stopWordList:
                reservedDocFreqMap[word] = docList
                reservedDocFreqyPtryMap[word] = freqyPtry
                reservedWordList.append(word)
        #for word
        
        sorted_tuples = sorted(reservedDocFreqyPtryMap.items(), key = lambda d:d[1], reverse = True)
        
        outFile = os.path.join(outDirPath, conference + ".docfreqy")  #output docfreqy
        outFileHandler = open(outFile, "w")
        for wordFreqyPtryTuple in sorted_tuples:
            word = wordFreqyPtryTuple[0]
            outFileHandler.write(word + ":")
            docList = reservedDocFreqMap[word]
            for doc in docList:
                outFileHandler.write(doc + " ")
            outFileHandler.write("\n")
        outFileHandler.close()
        
        outFile = os.path.join(outDirPath, conference + ".docfreqyptry")
        outFileHandler = open(outFile, "w")
        for wordFreqyPtryTuple in sorted_tuples:
            word = wordFreqyPtryTuple[0]
            outFileHandler.write(word + ":" + str(wordFreqyPtryTuple[1]) + "\n")
        #for
        
        outFile = os.path.join(outDirPath, conference + ".vocab")  #output vocab
        outFileHandler =  open(outFile, "w")
        for sorted_tuple in sorted_tuples:
            word = sorted_tuple[0]
            outFileHandler.write(word + "\n")
        #for
        
        if not os.path.exists(textOutDirPath):
            os.mkdir(textOutDirPath)
        
        for file in os.listdir(textInDirPath):
            inFilePath = os.path.join(textInDirPath, file)
            outFilePath = os.path.join(textOutDirPath, file)
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
        outFileHandler.close()
    #def


    def statDocFreqyAndVocab(self, subDirPath, conference):
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
        
        outFile = os.path.join(subDirPath, conference + ".docfreqy")  #output docfreqy
        outFileHandler = open(outFile, "w")
        for key in docFreqMap:
            outFileHandler.write(key + ":")
            docList = docFreqMap[key]
            for doc in docList:
                outFileHandler.write(doc + " ")
            outFileHandler.write("\n")
        outFileHandler.close()
        
        outFile = os.path.join(subDirPath, conference + ".vocab")  #output vocab
        outFileHandler =  open(outFile, "w")
        for key in docFreqMap:
            outFileHandler.write(key + "\n")
        #for
    #def


    def statDocFreqy(self, subDirPath, conference):
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
        
        outFile = os.path.join(subDirPath, conference + ".freqy")  #output docfreqy
        outFileHandler = open(outFile, "w")
        for key in docFreqMap:
            outFileHandler.write(key + ":")
            docList = docFreqMap[key]
            for doc in docList:
                outFileHandler.write(doc + " ")
            outFileHandler.write("\n")
        outFileHandler.close()
        
        #for
    #def

    def statDocFreqyPrty(self, subDirPath, conference):
        docFreqyFilePath = os.path.join(subDirPath, conference + ".docfreqy")
        docDirPath = os.path.join(subDirPath, conference);
        totalDocSize = len(os.listdir(docDirPath))
        
        wordFreqyMap = {}
        docFreqyFileHandler = open(docFreqyFilePath, "r")
        lines = docFreqyFileHandler.readlines()
        for line in lines:
            if len(line) <= 1 or ":" not in line:
                continue
            
            word_freqy = line.strip("\n").strip().split(":")
            if len(word_freqy) !=2:
                print(word_freqy)
                continue
            
            word = word_freqy[0]
            freqyList = word_freqy[1].split(" ")
            freqy = len(freqyList)
            wordFreqyMap[word] = freqy/totalDocSize
        #for line
        sorted_tuples = sorted(wordFreqyMap.items(), key = lambda d:d[1], reverse = True)
        docFreqyPrtyFilePath = os.path.join(subDirPath, conference + ".docfreqyptry")
        fileHandler = open(docFreqyPrtyFilePath, "w")
        for tuple in sorted_tuples:
            fileHandler.write(tuple[0]+":" + str(tuple[1]) + "\n")
        #for
        docFreqyFileHandler.close()
        fileHandler.close()
    #def
    
    def readMap(self, filePath, delimiter):
        
        dict = {}
        fileHandler = open(filePath, "r")
        lines = fileHandler.readlines()
        for line in lines:
            if len(line) < 2 or delimiter not in line:
                continue
            
            line = line.strip("\n").strip().split(delimiter)
            key = line[0]
            value = line[1]
            dict[key] = value
        #for
        
        return dict
    #def
    
    def readList(self, filePath):
        list = []
        fileHandler = open(filePath, "r")
        lines = fileHandler.readlines()
        for line in lines:
            if line == "" or line == "\n" or len(line) < 1:
                continue
            value = line.strip("\n").strip()
            list.append(value)
        #for
        return list
    #def
    
    def writeTupleList(self, filePath, tupleList, delimiter):
        fileHandler = open(filePath, "w")
        for tuple in tupleList:
            key = tuple[0]
            value = tuple[1]
            fileHandler.write(key + delimiter + value + "\n");
        #for
        fileHandler.close()
    #def
    
    def writeList(self, filePath, list, delimiter):
        fileHandler = open(filePath, "w")
        for value in list:
            fileHandler.write(value + delimiter)
        #for
        fileHandler.close()
    #def
    
    #predigest 
    def predigestDocBasedonFreqyPrty(self, subDirPath, conference, rootRootDir, outRootDir):
        
        print(subDirPath)
        
        docFreqyPtryFilePath = os.path.join(subDirPath, conference + ".docfreqyptry")
        docFreqyFilePath = os.path.join(subDirPath, conference + ".docfreqy")
        docDirPath = os.path.join(subDirPath, conference)
        stopWordListFile = os.path.join(rootRootDir, "en.txt")
        
        freqyPtryMap = self.readMap(docFreqyPtryFilePath, ":")
        sorted_tuples = sorted(freqyPtryMap.items(), key = lambda d:d[1])
        miniPtry = float(sorted_tuples[0][1])
        print(miniPtry)
        
        freqyMap = self.readMap(docFreqyFilePath, ":")
        
        stopWordList = self.readList(stopWordListFile)
        
        abandonedKeyList = []
        for key, value in freqyPtryMap.items():
            value = float(value)
            if key in stopWordList:      #stop word
                abandonedKeyList.append(key)
                continue;
            if value <= miniPtry:        #too few times
                abandonedKeyList.append(key)
                continue;
            if value >= self.freqyThreshold:  #too many times
                abandonedKeyList.append(key)
                continue;
        #for
        
        for key in abandonedKeyList:
            freqyPtryMap.pop(key)
        #for
        sorted_tupleList = sorted(freqyPtryMap.items(), key = lambda d:d[1], reverse = True)
        
        outDir = os.path.join(outRootDir, conference)
        if not os.path.exists(outDir):
            os.mkdir(outDir)
            
        outFreqyPtryFilePath = os.path.join(outDir, conference + ".docfreqyptry")
        self.writeTupleList(outFreqyPtryFilePath, sorted_tupleList, ":")
        
        docFreqyTupleList = []
        vocabList = []
        for sorted_tuple in sorted_tupleList:
            vocab = sorted_tuple[0]
            vocabList.append(vocab)
            
            if vocab not in freqyMap:
                print(vocab, " does not exist in map")
                continue
            
            freqy = freqyMap[vocab]
            docFreqyTupleList.append((vocab, freqy))
        #for sorted_tuple
        
        outFreqyFilePath = os.path.join(outDir, conference + ".docfreqy")
        self.writeTupleList(outFreqyFilePath, docFreqyTupleList, ":")
        outVocabFilePath = os.path.join(outDir, conference + ".vocab")
        self.writeList(outVocabFilePath, vocabList, "\n")
        
        outDocDirPath = os.path.join(outDir, conference)
        if not os.path.exists(outDocDirPath):
            os.mkdir(outDocDirPath)
        
        for file in os.listdir(docDirPath):
            filePath = os.path.join(docDirPath, file)
            fileHandler = open(filePath, "r")
            words = fileHandler.readline().strip("\n").strip().split()
            newLine = ""
            for word in words:
                if word in vocabList:
                    newLine = newLine + word + " "
            #for
            outFilePath = os.path.join(outDocDirPath, file)
            outDocFileHandler = open(outFilePath, "w")
            outDocFileHandler.write(newLine)
            outDocFileHandler.close()
        #for
    #def

    def statWordFreqy(self, inDirPath, outDirPath, conference):
        eta = 0.1
        vocabFilePath = os.path.join(inDirPath, conference + ".vocab")
        vocabList = self.readList(vocabFilePath)
        vocabSize = len(vocabList)
        
        totalWordNum = 0;
        wordFreqyMap = {}
        textInDirPath = os.path.join(inDirPath, conference)
        for file in os.listdir(textInDirPath):
            filePath = os.path.join(textInDirPath, file)
            fileHandler = open(filePath, "r")
            line = fileHandler.readline().strip("\n").strip()
            lines = line.split()
            
            for word in lines:
                totalWordNum = totalWordNum + 1
                if word in wordFreqyMap:
                    wordCount = wordFreqyMap[word]
                    wordFreqyMap[word] = wordCount + 1
                else:
                    wordFreqyMap[word] = 1
            #for
            fileHandler.close()
        #for
        
        outFile = os.path.join(outDirPath, conference + ".wordfreqy")  #output docfreqy
        outFileHandler = open(outFile, "w")
        sorted_tuples = sorted(wordFreqyMap.items(), key = lambda d:d[1], reverse = True)
        for eachTuple in sorted_tuples:
            word = eachTuple[0]
            freqy = eachTuple[1]
            freqyPrty = (freqy + eta)/(totalWordNum + eta * vocabSize)
            out = word + "," + str(freqy) + "," + str(freqyPrty) + "\n"
            outFileHandler.write(out)
        #for
        outFileHandler.close()
    #def

    def main(self):
        rootDir = r"C:\Users\dcsliub\Desktop\data"
        outRootDir = r"C:\Users\dcsliub\Desktop\data"
        
        rootRootDir = r"C:\Users\dcsliub\Desktop\data"
        stopWordPath = r"C:\Users\dcsliub\Desktop\en.txt"
        conferenceList = ["combinedtogether"]
        for conference in os.listdir(outRootDir):
            inDirPath = os.path.join(rootRootDir, conference)
            print(conference)
            outDirPath = os.path.join(outRootDir, conference)
            self.statWordFreqy(inDirPath, outDirPath, conference)
#             self.statDocFreqyAndVocabbasedonThreshold(inDirPath, outDirPath, conference, stopWordPath)

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
        