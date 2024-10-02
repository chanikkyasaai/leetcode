class Solution:
    def reverse(self, x: int) -> int:
        xstr = str(x)
        isneg = False
        if xstr[0] == '-':
            isneg = True
            xstr = xstr[1:]
        xstr = xstr[::-1]
        xnum = int(xstr)
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if isneg:
            xnum = xnum * -1

        if xnum < INT_MIN or xnum > INT_MAX:
            return 0
        
        return xnum
        