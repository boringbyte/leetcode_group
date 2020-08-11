'''
From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

 

Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
Example 2:

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
Example 3:

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
 

Constraints:

Both the source and target strings consist of only lowercase English letters from "a"-"z".
The lengths of source and target string are between 1 and 1000.
'''
import collections

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        s = collections.Counter(source)
        t = collections.Counter(target)
        for t_key in t.keys():
            if t_key not in s.keys():
                return -1
        
        target_pointer, source_length, target_length = 0, len(source), len(target)
        result = 0
        
        while target_pointer < target_length:
            source_pointer = 0

            while source_pointer < source_length and target_pointer < target_length:
                if target[target_pointer] == source[source_pointer]:
                    target_pointer += 1
                    source_pointer += 1
                else:
                    source_pointer += 1

            result += 1
        
        return result