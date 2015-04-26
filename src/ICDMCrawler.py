'''
Created on Apr 26, 2015

@author: dcsliub
'''
import os
import urllib.request
from bs4 import BeautifulSoup 

class ICDMCrawler:
    def crawlICDM(self, url, ouputDir, year): 
        opener = urllib.request.urlopen(url) 
        content = opener.read()
        content = content.decode('utf-8').encode('cp850', 'replace').decode('cp850')
        soup = BeautifulSoup(content)
        abstacts = soup.find_all('div', class_="panel-body")
        num = 0
        
        for abstract in abstacts:
            file = os.path.join(outputDir, year + str(num)+".txt")
            fileHandler = open(file, "w")
            try:
                fileHandler.write(abstract.text)
                fileHandler.close()
            except:
                print(num)
            num = num + 1 
        #for

url = "http://icdm2014.sfu.ca/program_accepted_papers.html" 
rootDir = "..\\icdm"
year = "14"
outputDir = os.path.join(rootDir, year)
icdmCrawler = ICDMCrawler()
icdmCrawler.crawlICDM(url, outputDir, year)
print("Program ends")