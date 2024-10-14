class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        x = len(flowerbed)
        for i in range(x):
            if n == 0:
                return True
            if flowerbed[i] == 0:
                if (i-1 < 0 or flowerbed[i-1] == 0) and (i+1 > x-1 or flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    n-=1
        if n== 0:
            return True
        
        return False