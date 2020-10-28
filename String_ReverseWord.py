'''
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include any extra spaces.
Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
'''
from collections import deque
class solution:
    def reverseWord(self,s:str) -> str:
        #approach 1 slit and reverse in place in python and then join
        return " ".join(reversed(s.split()))
        #Aproach 2 using deque
        left, right = 0, len(s) - 1
        
         #remove leading space
        while left <= right and s[left] == ' ':
            left += 1
         #remove trailing space
        while left <= right and s[right] == ' ':
            right += 1
        # push word by word in front of deque
        d,word = deque(), []
        while left <= right:
            if s[left] == ' 'and word:
                d.appendleft(' '.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1

        d.appendleft(''.join(word))

        return ' '.join(d)
            