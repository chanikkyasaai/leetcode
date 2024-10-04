class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ans = []
        n = len(skill)
        sum = skill[0] + skill[n-1]
        retsum = 0
        for i in range(n//2):
            if i >0 and sum != skill[i]+ skill[n-i-1]:
                return -1
            retsum += (skill[i]* skill[n-i-1])

        return retsum
        
            