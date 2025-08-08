class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = {}
        
        for i in range(len(nums)):
            if str(nums[i]) in count:
                count[str(nums[i])]+=1
            else:
               count[str(nums[i])]=1
        s = 0        
        for i in range(len(nums)):    
            if count[str(nums[i])] == 1:
                s+=nums[i]
            
        return s