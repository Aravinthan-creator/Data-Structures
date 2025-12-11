class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(int)

        for x in nums:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        
        for k, v in d.items():
            if v > 1:
                return True
        
        return False
        