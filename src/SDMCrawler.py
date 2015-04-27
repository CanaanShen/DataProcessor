'''
Created on Apr 26, 2015

@author: dcsliub
'''
import os
from bs4 import BeautifulSoup
import urllib.request
import re

class SDMCrawler:
    def crawlSDM(self, url, outputDir, year):
        
        head = {
       'Connection': 'Keep-Alive',
       'Accept': 'text/html, application/xhtml+xml, */*',
       'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
       'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        }
        opener = urllib.request.build_opener()
        header = []
        for key, value in head.items():
            elem = (key, value)
            header.append(elem)
        opener.addheaders = header
        
        for num in range(1, 123):
            newURL = url + "." + str(num)
            print(newURL)
            
            content = opener.open(newURL).read()
            content = content.decode('utf-8').encode('cp850', 'replace').decode('cp850')
            soup = BeautifulSoup(content)
            print(content)
#            abstract = soup.find('div', attrs={'class':'abstractSection'})
#             print(abstract)

        
    #def
#class

url = "http://epubs.siam.org/doi/book/10.1137/1.9781611973440"
rootDir = "..\\sdm"
year = "14"
outputDir = os.path.join(rootDir, year)

if not os.path.exists(outputDir):
    os.mkdir(outputDir)

sdmCrawler = SDMCrawler()
sdmCrawler.crawlSDM(url, outputDir, year)
print("Program ends")