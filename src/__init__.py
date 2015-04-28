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
        str1 = "aadddcc"
        if " " not in str1:
            print(str1)
#         if str1.isalpha():
#             print(str1)
        
        str2 = "aa"
#         print(str1.strip(" "))
#         if str1 is str2:
#             print(str1)
         
tester = Tester()
tester.test()
print("Program Ends")