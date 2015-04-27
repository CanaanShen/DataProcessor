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
        word = "AccB-dd-Ed"
        word = word.replace("-", "")
        print(word)
         
tester = Tester()
tester.test()
print("Program Ends")