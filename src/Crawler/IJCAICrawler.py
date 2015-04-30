'''
Created on Apr 21, 2015

@author: dcsliub
'''

import urllib.request
import re
import os
from bs4 import BeautifulSoup

class IJCAICrawler:

    def crawlURL(self, url, year, outputDir):
        opener = urllib.request.urlopen(url)
        content = opener.read()
        content = content.decode('utf-8').encode('cp850', 'replace').decode('cp850')
        soup = BeautifulSoup(content)
        #print(soup.find('body'))#correct
        num = 0
        for link in soup.findAll('a', href=re.compile('Abstracts/.*.html$')):
            eachPaperURL = link['href']
            eachPaperURL = "http://ijcai.org/papers" + year +"/" + eachPaperURL

            try:
                eachPaperOpener = urllib.request.urlopen(eachPaperURL)
                eachPaperContent = eachPaperOpener.read()
                eachPaperContent.decode('utf-8').encode('cp850', 'replace').decode('cp850')
                soup = BeautifulSoup(eachPaperContent)
#                 #pContent = soup.find_all('div')#.findAll("p")[1].text
                mainContent = soup.find_all("p")
                author = mainContent[0].text
                abstract = mainContent[1].text
                print(author)
#                 
                outputFilePath = os.path.join(outputDir, year+str(num) + ".txt")
                outputFileHandler = open(outputFilePath, "w")
                outputFileHandler.write(abstract)
                outputFileHandler.close()
                num = num + 1
#                 for div in divList:
#                     #print(div.get("class"))
#                     
#                     if "pabstract" in str(div['class']):
#                         outputFilePath = os.path.join(outputDir, year+str(num) + ".txt")
#                         outputFileHandler = open(outputFilePath, "w")
#                         outputFileHandler.write(div.text)
#                         outputFileHandler.close()
#                         num = num + 1
#                         print(num)
#                 title = pContent[0].text
#                 print(title)
#                 abstract = pContent[2].text
#                 print(abstract)

            except:
                print(eachPaperURL)
                
    def crawlURL2(self, url, year, outputDir):
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
        #url = "http://www.aaai.org/ocs/index.php/AAAI/AAAI12/paper/view/5087"
        url = "http://ijcai.org/papers13/Abstracts/014.html"
        data = opener.open(url).read()
        content = data.decode('utf-8').encode('cp850', 'replace').decode('cp850')
        soup = BeautifulSoup(content)
        
        print(soup.find("body"))
#         num = 0
#         for link in soup.findAll('a', href=re.compile('Abstracts/.*.html$')):
#             eachPaperURL = link['href']
#             eachPaperURL = "http://ijcai.org/papers" + year +"/" + eachPaperURL
# 
#             try:
#                 eachPaperOpener = urllib.request.urlopen(eachPaperURL)
#                 eachPaperContent = eachPaperOpener.read()
#                 eachPaperContent.decode('utf-8').encode('cp850', 'replace').decode('cp850')
#                 soup = BeautifulSoup(eachPaperContent)
# #                 #pContent = soup.find_all('div')#.findAll("p")[1].text
#                 mainContent = soup.find_all("p")
#                 author = mainContent[0].text
#                 abstract = mainContent[1].text
#                 print(author)
# #                 
#                 outputFilePath = os.path.join(outputDir, year+str(num) + ".txt")
#                 outputFileHandler = open(outputFilePath, "w")
#                 outputFileHandler.write(abstract)
#                 outputFileHandler.close()
#                 num = num + 1
# 
#             except:
#                 print(eachPaperURL)
#class
ijcaiCrawler = IJCAICrawler()
year = "05"
url = "http://dl.acm.org/citation.cfm?id=1642293&picked=prox&cfid=483719804&cftoken=47431823"
rootDir = "..\\ijcaitxt"
outputDir = os.path.join(rootDir, year)

ijcaiCrawler.crawlURL2(url, year, outputDir)
print("Program ends")