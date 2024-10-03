class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i = 0
        j = k-1
        vowels = ('a','e','i','o','u')
        maxv = 0
        for x in range(j+1):
            if s[x] in vowels:
                maxv+=1
        i = 1
        j = j+1
        cn = maxv
        while j< len(s):
            if s[i-1] in vowels:
                cn-=1
            if s[j] in vowels:
                cn+=1
            maxv = max(maxv,cn)
            i+=1
            j+=1
        return maxv
