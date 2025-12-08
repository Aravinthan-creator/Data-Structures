class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0 
        for i in range (3,n):
           for j in range(i+1,n):
               s = i*i + j*j
               k = int(s**0.5)
               if k<= n :
                  if k*k == s:
                      ans += 2
               else:
                     break
        return ans                  