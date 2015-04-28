'''
Created on Apr 26, 2015

@author: dcsliub
'''
import os
import urllib.request
import re
from bs4 import BeautifulSoup

class ACLCrawler:
    def crawlACL(self, url, outputDir, year):
        opener = urllib.request.urlopen(url)
        content = opener.read()
        content = content.decode('utf-8').encode('cp850', 'replace').decode('cp850')
        soup = BeautifulSoup(content)
        latexmlLinks = soup.find_all('a', text="latexml")
        num = 0
        
        for latexmlLink in latexmlLinks:
            link = latexmlLink.get('href')
            fullLink = url + link
            
            opener = urllib.request.urlopen(fullLink)
            content = opener.read()
            content = content.decode('utf-8').encode('cp850', 'replace').decode('cp850')
            soup = BeautifulSoup(content)
            abstract = soup.find('p', class_="ltx_p").text
            
            file = os.path.join(outputDir, year + str(num)+".txt")
            fileHandler = open(file, "w")
            fileHandler.write(abstract)
            fileHandler.close()
            num = num + 1
        #for

    #def
    def crawlACL13(self, url, outputDir, year, conference):
        opener = urllib.request.urlopen(url)
        content = opener.read()
        content = content.decode('utf-8').encode('cp850', 'replace').decode('cp850')
        soup = BeautifulSoup(content)
        paperLinks = soup.find_all('a', href=re.compile("accepted/\d+.html"))
        num = 0
        
        for paperLink in paperLinks:
            link = paperLink.get('href')
            fullLink = conference + link
            
            opener = urllib.request.urlopen(fullLink)
            content = opener.read()
            content = content.decode('utf-8').encode('cp850', 'replace').decode('cp850')
            soup = BeautifulSoup(content)
            div = soup.find_all("div")
            
            abstract = ""
            for content in div[0].p.br.p.p.contents:
                content = str(content)

                if "<" in content and ">" in content:
                    print(content)
                else:
                    abstract = abstract + content
            #for
            
            file = os.path.join(outputDir, year + str(num)+".txt")
            fileHandler = open(file, "w")
            fileHandler.write(abstract)
            fileHandler.close()
            num = num + 1
        #for

    #def
#class

url = "http://acl2013.org/site/accepted-papers.html"
rootDir = "..\\acl"
year = "13"
outputDir = os.path.join(rootDir, year)
conference = "http://acl2013.org/site/"
aclCrawler = ACLCrawler()
aclCrawler.crawlACL13(url, outputDir, year, conference)
print("Program ends")
