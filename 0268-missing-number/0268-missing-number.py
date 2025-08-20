class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        asum=n*(n+1)//2
        gsum= sum(nums)
        return asum - gsum