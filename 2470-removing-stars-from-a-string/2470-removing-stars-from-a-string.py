class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        j= -1

        for i in s:
            if i is '*' and j>-1 :
                stack.pop()
            else:
                stack.append(i)
                j+=1
        return ''.join(stack)