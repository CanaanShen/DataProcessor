'''
Created on Apr 21, 2015

@author: dcsliub
'''
import csv
import os

from _operator import delitem

class AAAICSVReader:
    
    def readCSV(self, inputFile, outputDir, conference):
        
        with open(inputFile) as csvfile:
            reader = csv.reader(csvfile)
            num = 0
            #for title, keywords, topics, highlevel, abstract in reader:  #aaai13
            for title, authors, groups, keywords, topics, abstract in reader:
                outputFile = os.path.join(outputDir, conference + str(num))
                outputFileHandler = open(outputFile, "w")
                outputFileHandler.write(abstract)
                num = num + 1
                outputFileHandler.close()
            #for
        
    #def
    
reader = AAAICSVReader()

inputFile = "..\\mallet\\aaai14.csv"
ouputDir = "..\\mallet\\aaaiabstract"
conference = "aaai14"
reader.readCSV(inputFile, ouputDir, conference)
print("Program ends")
#class
