class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

       res = nums[0]
       maxv= nums[0]
       
       for i in range (1, len(nums)):
            maxv = max(maxv+nums[i], nums[i]) 
            res = max(res,maxv)
            
       return res