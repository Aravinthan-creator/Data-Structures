class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0 
        left = 0
        right =len(height)-1 
        while left < right :
                d = (right - left) 
                v = min (height[right] ,height[left]) 
                sh = d*v
                ans = max(ans ,sh)
                if height[right]>height[left]:
                    left+=1
                else: 
                    right-=1
        return ans 


