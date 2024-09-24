class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        pnt1 = 0
        pnt2 = 1

        while pnt1 < len(asteroids) and pnt1>=0 and pnt2 < len(asteroids):
            if asteroids[pnt1] > 0 and asteroids[pnt2] <0:
                if abs(asteroids[pnt2]) < asteroids[pnt1]:
                    del asteroids[pnt2]
                    if pnt1-1 >=0 and pnt2-1 >= 0:
                        pnt1-=1
                        pnt2-=1
                    continue
                elif abs(asteroids[pnt2]) > asteroids[pnt1]:
                    del asteroids[pnt1]
                    if pnt1-1 >=0 and pnt2-1 >= 0:
                        pnt1-=1
                        pnt2-=1
                    continue
                else:
                    del asteroids[pnt1:pnt2+1]
                    if pnt1-1 >=0 and pnt2-1 >= 0:
                        pnt1-=1
                        pnt2-=1
                    continue
            pnt1+=1
            pnt2+=1

        return asteroids