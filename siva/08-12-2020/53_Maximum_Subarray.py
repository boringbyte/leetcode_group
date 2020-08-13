'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return
        n = len(nums)
        dp = [None] * n
        result = dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            result = max(dp[i], result)
        return result