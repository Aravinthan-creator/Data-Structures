class Solution:
    def rob(self, nums: List[int]) -> int:
        [2,1]
        [2,2]
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * (n)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return max(dp[n-1], dp[n-2])