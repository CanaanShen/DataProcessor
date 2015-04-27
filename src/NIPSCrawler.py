'''
Created on Apr 26, 2015

@author: dcsliub
'''

import os
from bs4 import BeautifulSoup
import urllib.request
import re

class NIPSCrawler:
    def crawlNIPS(self, url, outputDir, year, prefix):
        
        opener = urllib.request.urlopen(url)
        content = opener.read()
        content = content.decode('utf-8').encode('cp850', 'replace').decode('cp850')
        soup = BeautifulSoup(content)
        paperLinks = soup.find_all('a', href=re.compile('/paper/\d+.*'))
        
        num = 0
        for paperLink in paperLinks:
            paperURL = paperLink.get('href')
            paperURL = prefix + paperURL
            
            opener = urllib.request.urlopen(paperURL)
            content = opener.read()
            content = content.decode('utf-8').encode('cp850', 'replace').decode('cp850')
            soup = BeautifulSoup(content)
            abstract = soup.find('p', attrs={'class':'abstract'}).text
            
            outputFilePath = os.path.join(outputDir, year + str(num) + ".txt")
            outputFileHandler = open(outputFilePath, "w")
            outputFileHandler.write(abstract)
            outputFileHandler.close()
            num = num + 1
        #for
    #def
#class
url = "http://papers.nips.cc/book/advances-in-neural-information-processing-systems-22-2009"
rootDir = "..\\nips"
year = "09"
prefix = "http://papers.nips.cc"
outputDir = os.path.join(rootDir, year)

if not os.path.exists(outputDir):
    os.mkdir(outputDir)

nipsCrawler = NIPSCrawler()
nipsCrawler.crawlNIPS(url, outputDir, year, prefix)
print("Program ends")