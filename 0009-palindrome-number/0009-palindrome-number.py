class Solution:
    def isPalindrome(self, x: int) -> bool:
        # num = str(x)
        # n = len(num)

        # for i in range(n//2):
        #     if num[i] != num[n-i-1]:
        #         return False
        # return True
        if x < 0:
            return False
        nx = str(x)
        num = int(nx[::-1])
        if x == num:
            return True
        else:
            return False