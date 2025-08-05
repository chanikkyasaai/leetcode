class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # countS, countT = {}, {}

        # if len(s) != len(t):
        #     return False

        # for i in s:
        #     if i not in countS:
        #         countS[i] = 1
        #     else:
        #         countS[i] +=1

        # for i in t:
        #     if i not in countT:
        #         countT[i] = 1
        #     else:
        #         countT[i] +=1
        # return countS == countT
                
        # return sorted(s) == sorted(t)
        if len(s)!= len(t):
            return False
        sr = [0]*26

        for i in range(len(s)):
            sr[ord(s[i])-ord('a')]+=1
            sr[ord(t[i]) - ord('a')]-=1
        
        for i in sr:
            if i!= 0:
                return False
    
        return True

        return sr == tr