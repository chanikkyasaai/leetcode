class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        n = len(num)

        for i in range(n//2):
            if num[i] != num[n-i-1]:
                return False
        return True