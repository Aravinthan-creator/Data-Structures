class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            target = -nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[j] + nums[k]
                
                if s == target:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                        
                elif s < target:
                    j += 1
                else:
                    k -= 1
        
        return ans
