class Solution:
    def minimumSteps(self, s: str) -> int:
        swap = 0
        black = 0

        for i in s:
            if i == '1':
                black+=1
            else:
                swap+= black
        return swap
