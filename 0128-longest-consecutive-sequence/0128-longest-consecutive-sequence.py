class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        v = 0

        for x in s:
            if x-1 not in s:
                cs=1
                c=x
                while c+1 in s:
                    cs+=1
                    c+=1
                v = max(cs,v)
        return v