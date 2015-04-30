'''
Created on Apr 21, 2015

@author: dcsliub
'''

import urllib.request
import re
import os
from bs4 import BeautifulSoup

class AAAICrawler:

    def crawlURL(self, url, outputDir, year):
        opener = urllib.request.urlopen(url)
        content = opener.read()
        content = content.decode('utf-8').encode('cp850', 'replace').decode('cp850')
        soup = BeautifulSoup(content)
        #print(soup.find('body'))#correct
        
        num = 0
        for link in soup.findAll('a', href=re.compile('http://www.aaai.org/ocs/index.php/AAAI/AAAI' + year + '/paper/view/\d+$')):
            
            outputFile = os.path.join(outputDir, year, str(num) +".txt")
            print(str(num))

            if os.path.exists(outputFile): 
                continue

            eachPaperURL = link['href']
             
            eachPaperOpener = urllib.request.urlopen(eachPaperURL)
            eachPaperContent = eachPaperOpener.read()
            eachPaperContent.decode('utf-8').encode('cp850', 'replace').decode('cp850')
            soup = BeautifulSoup(eachPaperContent)
            frame = soup.find_all("frame")
            abstractURL = frame[0].get("src")
            #print(abstractURL)
            
            abstactOpener = urllib.request.urlopen(abstractURL)
            abstractContent = abstactOpener.read()
            abstractContent.decode("utf-8").encode("cp850", "replace").decode("cp850")
            soup = BeautifulSoup(abstractContent)
            try:
                abstract = soup.find('div', id="abstract").find('div').text #.get_text()
               
                outputFileHandler = open(outputFile, "w")
                outputFileHandler.write(abstract)
                outputFileHandler.close()
            except:
                print(str(num) + " expection")

            num = num + 1

#class
aaaiCrawler = AAAICrawler()
outputDir = "C:\\Users\\dcsliub\\Desktop\\abstactdata\\aaai\\text"
year = "14"
url = "http://www.aaai.org/ocs/index.php/AAAI/AAAI" + year + "/schedConf/presentations"
aaaiCrawler.crawlURL(url, outputDir, year)
print("Program ends")