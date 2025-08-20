class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1=len(nums1)
        n2=len(nums2)
        res =set()
        for i in range(n1):
            for j in range(n2):
                if nums1[i]==nums2[j]:
                    res.add(nums1[i])
        return list(res)