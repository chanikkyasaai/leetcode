class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        noofclosed = 0
        openb = 0
        for i in s:
            if i == ')':
                if openb == 0:
                    noofclosed+=1
                else:
                    openb-=1
            elif i == '(':
                openb+=1

        return noofclosed + openb