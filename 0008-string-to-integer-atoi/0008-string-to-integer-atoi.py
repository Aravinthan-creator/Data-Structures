class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        res = 0
        sign = 1
        
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        # 1. Skip leading spaces
        while i < n and s[i] == " ":
            i += 1
        
        # 2. Check sign
        if i < n and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                sign = -1
            i += 1
        
        # 3. Process digits
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # 4. Check overflow before it happens
            if res > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            res = res * 10 + digit
            i += 1
        
        return sign * res
