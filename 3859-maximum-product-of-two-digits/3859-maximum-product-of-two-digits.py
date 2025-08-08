class Solution:
    def maxProduct(self, n: int) -> int:
        arr = []
        ld =0 
       
        while n:
            ld = n%10
            arr.append(ld)
            n = n//10
            
       
        m1 = max(arr)
        arr.remove(m1)
        m2 = max(arr)
        
        return m1 * m2
                                      
               