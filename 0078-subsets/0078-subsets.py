class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def sub(i):
            if i == len(nums):
                res.append(subset[:])
                return
            
            sub(i+1)
            subset.append(nums[i])
                    
            sub(i+1)
            subset.pop()
        
        sub(0)
        
        return res