'''

Created on Apr 22, 2015

@author: dcsliub
'''
import urllib.request
import os
from bs4 import BeautifulSoup

class JMLRCrawler:
    
    def crawler(self, url, conference, volume, outputDir):
        opener = urllib.request.urlopen(url)
        content = opener.read()
        content = content.decode('utf-8').encode('cp850', 'replace').decode('cp850')
        soup = BeautifulSoup(content)
        allABSLinks = soup.find_all('a', text="abs")
        num = 0
        
        for link in allABSLinks:
            absLink = link.get('href')
            if not "http://www.jmlr.org/" in absLink:
                absLink = conference + absLink
            
            opener = urllib.request.urlopen(absLink)
            content = opener.read()
            content = content.decode('utf-8').encode('cp850', 'replace').decode('cp850')
            soup = BeautifulSoup(content)
            
            fullAbstract = ""
            abstract = soup.find('div', id = 'content')
            contentLen = len(abstract.contents)
            
            i = 6
            while True:
                subABS = abstract.contents[i]
                if "<" in str(subABS) and ">" in str(subABS):
                    subABS = subABS.text
                
                if "[abs]" in subABS:
                    subABS = subABS.replace("[abs]", "")
                if "[" in subABS:
                    subABS = subABS.replace("[", "")
                
                fullAbstract = fullAbstract + " " + str(subABS)
                i = i + 1
                
                if i >= contentLen - 4:
                    break
#             #while
            
            try:
                file = os.path.join(outputDir, str(volume) + str(num) + ".txt")
                fileHandler = open(file, "w")
                fileHandler.write(fullAbstract)
                fileHandler.close()

            except:
                print(str(num))
            num = num + 1
        #for
    #def
#class  
volume = 7
conference = "http://jmlr.csail.mit.edu"
url = "http://jmlr.csail.mit.edu/papers/v" + str(volume) + "/"
rootDir = "..\\jmlr"
outputDir = os.path.join(rootDir, str(volume))

if not os.path.exists(outputDir):
    os.mkdir(outputDir)

jmlrCrawler = JMLRCrawler()
jmlrCrawler.crawler(url, conference, volume, outputDir)
print("Program ends")