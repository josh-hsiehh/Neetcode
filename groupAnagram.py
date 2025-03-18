from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #create dictionary
        res = defaultdict(list)

        #iterate through strings
        for s in strs:

            #array with 26 spaces for each lowercase letter, each defaulted to the value 0
            count = [0]*26

            #iterate through characters
            for c in s:

                #add 1 when finding a specific character
                count[ord(c)-ord('a')]+=1

            #append all strings that have the same characters, (anagram)    
            res[tuple(count)].append(s)
        
        #return the dictionary
        return list(res.values())

