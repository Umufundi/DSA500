
'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''


from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #check edge case for invalid input 
        if len(s) != len(t):
            return False
        
        #initalize counters using defaultdict
        countS, countT = defaultdict(int), defaultdict(int)

        #loop range(len(s)) times while counting each occurrence 
        for i in range(len(s)):
            countS[s[i]] += 1
            countT[t[i]] += 1

        # return whether the counters are equal or not (TRUE/FALSE)
        return countS == countT
