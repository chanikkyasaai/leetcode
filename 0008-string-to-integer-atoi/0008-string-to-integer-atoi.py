class Solution:
    def myAtoi(self, s: str) -> int:
        isneg = False
        s = s.lstrip()
        i=0
        num = ""

        if len(s) > 0 and s[i] == '-':
            isneg = True
            i+=1
        elif len(s) > 0 and s[i] == '+':
            i+=1

        while i < len(s):
            if not s[i].isdigit():
                break
            num+=s[i]
            i+=1

        if len(num) > 0 and num[0] == '0':
            num = num[1:]

        if len(num) == 0:
            return 0
        
        num = int(num)

        if isneg:
            num = num * -1
        
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if num < INT_MIN:
            return INT_MIN
        elif num > INT_MAX:
            return INT_MAX
        else:
            return num
        

        