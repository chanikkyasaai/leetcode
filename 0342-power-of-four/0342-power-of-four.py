class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        return True if math.log(n,4)%1 == 0 else False