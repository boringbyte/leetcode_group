'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

# Top Down Recursion

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        
# Top Down with Memonization

class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = dict()
        
        def recursive(n):
            if n == 1 or n == 2:
                return n
            elif n in memo:
                return memo[n]
            else:
                memo[n] = recursive(n - 1) + recursive(n - 2)
                return memo[n]
        
        return recursive(n)

# Top Down DP

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        
        DP = [None] * n
        DP[0], DP[1] = 1, 2
        
        for i in range(2, n):
            DP[i] = DP[i - 1] + DP[i - 2]
        return DP[-1]
        