class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        right = len(s) - 1
        flag = False
        cnt = 0 
        while right >=0:
            if s[right] != " " and flag == False:
                flag = True 
            if s[right] == " " and flag == True:
                return cnt 
            if flag == True:
                cnt += 1
            right -= 1
        return cnt  
           
        