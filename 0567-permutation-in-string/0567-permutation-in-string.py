class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)

        s1count = [0]*26
        wincount = [0]*26

        def charindex(ch):
            return ord(ch) - ord("a")

        for ch in s1:
            s1count[charindex(ch)]+=1

        for i in range(len(s2)):
            wincount[charindex(s2[i])] +=1

            if i>= m:
                wincount[charindex(s2[i - m])]-=1
            if s1count == wincount:
                return True
        return False