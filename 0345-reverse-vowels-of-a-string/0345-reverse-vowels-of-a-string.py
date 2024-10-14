class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        s = list(s)
        vowels = ['a','e','i','o','u']
        vowind = []
        for i in range(n):
            if s[i].lower() in vowels:
                vowind.append(i)
        
        x = len(vowind)
        for i in range(x//2):
            s[vowind[i]], s[vowind[x-i-1]] = s[vowind[x-i-1]], s[vowind[i]]
        return ''.join(s)

