'''
Created on Apr 26, 2015

@author: dcsliub
'''
import os
import urllib.request
from bs4 import BeautifulSoup

class ACLCrawler:
    def crawlACL(self, url, outputDir, year):
        opener = urllib.request.urlopen(url)
        content = opener.read()
        soup = BeautifulSoup(content)
        latexmlLinks = soup.find_all('a', text="")

    #def
#class

url = "https://www.aclweb.org/anthology/P/P14/"
rootDir = "..\\acl"
year = "14"
outputDir = os.path.join(rootDir, year)
aclCrawler = ACLCrawler()
aclCrawler.crawlACL(url, outputDir, year)
print("Program ends")
