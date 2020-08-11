'''
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

 

Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
Example 2:

Input: s = "1326#"
Output: "acz"
Example 3:

Input: s = "25#"
Output: "y"
Example 4:

Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output: "abcdefghijklmnopqrstuvwxyz"
'''

import string

class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        result, n, i = [], len(s), 0
        
        mapper = {str(i + 1): c for i, c in enumerate(string.ascii_lowercase)}
        
        while i < n:
            if i + 2 < n and s[i+2] == '#':
                result.append(mapper[s[i: i+2]])
                i += 3
            else:
                result.append(mapper[s[i]])
                i += 1
                
        return ''.join(result)