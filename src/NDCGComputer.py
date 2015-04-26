'''
Created on Dec 14, 2014

@author: dcsliub
'''
import math

class NDCGComputer:
    
    def computeDCG(self, relevanceList):
        
        size = len(relevanceList)
        DCG = 0.0
        for i in range(size):
            
            rel_score = relevanceList[i]
            position = i+1;
            
            numerator = pow(2, rel_score) - 1
            denominator = math.log2(position + 1)
            DCG = DCG + numerator/denominator;
        #for ends
        
        return DCG
    #def
    
    def computeNDCG(self, modelPrefix, domainfix, inputFileSuffix, outputFileSuffix):
        
        inputFilePath = modelPrefix + domainfix + inputFileSuffix
        outputFilePath = modelPrefix + domainfix + outputFileSuffix
        
        print("fileName " + str(inputFilePath))
        inputFileHandler = open(inputFilePath, "r")
        outputFileHandler = open(outputFilePath, "w")
        
        topicsCount = 0
        totalNDCG = 0.0
        line = " "
        while len(line) != 0:
            line = inputFileHandler.readline().strip("\n")
            
            if len(line) < 3:
                continue
            
            relevanceString = line.split(";")
            
            if len(relevanceString) < 2:
                print("splitting errors")
                break;
            
            realRelevanceString = relevanceString[0].strip()
            idealRelevanceString = relevanceString[1].strip()
            
            realRelevanceStrList = []
            idealRelevanceStrList = []
            
            realRelevanceStrList = realRelevanceString.split(" ");
            idealRelevanceStrList = idealRelevanceString.split(" ")
            
            realRelevanceNumList = []
            idealRelevanceNumList = []
            
            for realRelevanceStr in realRelevanceStrList:
                realRelevanceNumList.append(float(realRelevanceStr))
            
            for idealRelevanceStr in idealRelevanceStrList:
                idealRelevanceNumList.append(float(idealRelevanceStr))
            
            DCG = self.computeDCG(realRelevanceNumList)
            iDCG = self.computeDCG(idealRelevanceNumList)
            nDCG = DCG/iDCG
            
            outputFileHandler.write(str(nDCG) + "\n")
            totalNDCG = totalNDCG + nDCG
            
            topicsCount = topicsCount + 1
            print(str(topicsCount) + " : " + str(nDCG))
        #while ends
        averageNDCG = totalNDCG/topicsCount
        outputFileHandler.write("average: " + str(averageNDCG) + "\n")
        print("average: " + str(averageNDCG))
              
        inputFileHandler.close()
        outputFileHandler.close()
        
    #def ends
#class ends

folderFix = "..//data//"

domainList = []
domainList.append("Battery")
#domainList.append("Camera")
modelName = "RankLDA"
n = 10
for domain in domainList:
    
    modelPrefix = folderFix + modelName + "//" + modelName
    domainfix = "_" + domain + "_"
    inputFileSuffix = "Relevance@" + str(n) + ".txt"
    outputFileSuffix = "NDCG@" + str(n) + ".txt"

    ndcgComputer = NDCGComputer()
    ndcgComputer.computeNDCG(modelPrefix, domainfix, inputFileSuffix, outputFileSuffix)

print("Program ends")