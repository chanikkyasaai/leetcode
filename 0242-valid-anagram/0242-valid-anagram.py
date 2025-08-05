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

        sr = [0]*26
        tr = [0]*26

        for i in s:
            sr[ord(i)-ord('a')]+=1
        for i in t:
            tr[ord(i)-ord('a')]+=1
        return sr == tr