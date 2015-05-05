# -*- coding: utf-8 -*-
'''
Created on Apr 29, 2015

@author: dcsliub
'''
import urllib.request
import os
from bs4 import BeautifulSoup

class ICMLCrawler:
    def Crawl14and13(self, url, conference, year, outputDir, prefix):
        opener = urllib.request.urlopen(url)
        content = opener.read()
        soup = BeautifulSoup(content)
        allABSLinks = soup.find_all('a', text="abs")
        num = 0
        
        for link in allABSLinks:
            absLink = link.get('href')
            absLink = prefix + absLink
            
            opener = urllib.request.urlopen(absLink)
            content = opener.read()
            soup = BeautifulSoup(content)
            
            fullAbstract = ""
            abstract = soup.find('div', id = 'abstract')
            for content in abstract.contents:
                
                if "</" in str(content) and ">" in str(content): #tag
                    content = content.text
                
                fullAbstract = fullAbstract + content + " "
            #for
            
            try:
                file = os.path.join(outputDir, conference + year + str(num) + ".txt")
                fileHandler = open(file, "w")
                fileHandler.write(fullAbstract)
                fileHandler.close()

            except:
                print(str(num) + " exception")
            num = num + 1
        #for
    #def
    def Crawl12and11and10(self, url, conference, year, outputDir):
        
        opener = urllib.request.urlopen(url)
        content = opener.read()
        soup = BeautifulSoup(content)
        allP = soup.find_all('p', attrs={'class':'abstracts'})

        num = 0
        for eachP in allP:
            abstract = ""
            for content in eachP.contents:
                if "<" in str(content) and ">" in str(content):
                    continue
                else:
                    abstract = abstract + content + " "
            #for
            try:
                file = os.path.join(outputDir, conference + year + str(num) + ".txt")
                fileHandler = open(file, "w")
                fileHandler.write(abstract)
                fileHandler.close()

            except:
                print(str(num) + " exception")
            num = num + 1
    #def

year = "10"
conference = "icml"
url = "http://www.icml2010.org/abstracts.html"
rootDir = "..\\icml"
# prefix = "http://jmlr.org/proceedings/papers/v28/"
outputDir = os.path.join(rootDir, str(year))

if not os.path.exists(outputDir):
    os.mkdir(outputDir)

icmlCrawler = ICMLCrawler()
icmlCrawler.Crawl12and11and10(url, conference, year, outputDir)
print("Program ends")