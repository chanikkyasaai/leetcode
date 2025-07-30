from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # m = len(s)
        # n = len(p)
        # ans = []

        # p_count = Counter(p)
        # s_count = Counter(s[:n])

        # if s_count==p_count:
        #     ans.append(0)
        # for i in range(n,m):
        #     schar = s[i-n]
        #     nchar = s[i]

        #     s_count[schar]-=1
        #     if s_count[schar]== 0:
        #         del s_count[schar]
            
        #     s_count[nchar]+=1
        #     if s_count == p_count:
        #         ans.append(i-n+1)
        
        # return ans
        if len(p) > len(s):
            return []

        def char_index(c):
            return ord(c) - ord('a')

        p_count = [0] * 26
        s_count = [0] * 26

        for ch in p:
            p_count[char_index(ch)] += 1

        res = []

        for i in range(len(s)):
            s_count[char_index(s[i])] += 1

            if i >= len(p):
                s_count[char_index(s[i - len(p)])] -= 1

            if s_count == p_count:
                res.append(i - len(p) + 1)

        return res
