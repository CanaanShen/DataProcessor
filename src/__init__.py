'''
Created on Oct 19, 2014

@author: xyshen
'''
import math
import re
from decimal import Decimal
class Tester:

    def __init__(self):
        '''
        Constructor
        '''
        self.userCount = 23152
    
    def test(self):
#         str = "aaa bbb ccc  ddd     "
#         words = str.split()
#         print(words)
#         for word in words:
#             print(word)
#         word = "AccB-dd-Ed"
#         word = word.replace("-", "")
#         print(word)
#         str1 = "aadd\"dcc"
#         if "\"" in str1:
#             print(str1)
# #         if str1.isalpha():
# #             print(str1)
#         
#         str2 = "aa"
#         print(str1.strip(" "))
#         if str1 is str2:
#             print(str1)
#         num = 291
#         num1 = num/2
#         print(num1)
#         str = " aaaa    "
#         results = str.split()
#         print(results)
#         for result in results:
#             print(result)
#         word = "aaa"
#         if "aaa" in word:
#             print(word)
#         blankWords = word.split()
#         word = ""
#         for blankWord in blankWords:
#             if blankWord.isalpha():                #English word
#                 word = word + blankWord + " "
#         print(word)
#         map = {}
#         map["aa"] = 1
#         map["bb"] = 2
#         if "bb" in map:
#             print(map["bb"])
#         str = "aa bb cc"
#         if "a" in str:
#             print(str)
#         docFreqMap = {}
#         docFreqMap["aa"] = 3
#         docFreqMap["cc"] = 1
#         docFreqMap["nn"] = 10
#         docFreqMap["ll"] = 8
#         print(docFreqMap.pop("cc"))
#         print(docFreqMap)
#         
#         for (key, value) in docFreqMap.items():
#             print(key, value)
#         
#         sortedList = sorted(docFreqMap.items(), key=lambda d:d[1], reverse = True)
#         print(sortedList[2])
#         str = "1828.txt";
#         print(str.replace(".txt", ""))
#         for tuple in sortedList:
#             print(tuple[0])
#         regex = re.compile("^[a-z]+$")
#         blankWord = "wo33rd"
#         if regex.match(blankWord):
#             print(blankWord)
#         dict = {}
#         dict["aaa"] = 3
#         dict["bbb"] = 10
#         dict["ccc"] = 4
#         print(dict)
#         dict.pop("bbb")
#         print(dict)
#         p = "0.12"
#         p = float(p)
#         print(p)
#         sorted_tuples = sorted(dict.items(), key = lambda d:d[1], reverse = True)
#         for tuple in sorted_tuples:
#             print(tuple[0], tuple[1])
        tupleList = []
        tupleList.append(("aaa", 2))
        tupleList.append(("bbb", 5))
        print(tupleList)
    #def 
         
tester = Tester()
tester.test()
print("Program Ends")