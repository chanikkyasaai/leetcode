class Solution:
    def reverseWords(self, s: str) -> str:
        words = list(s.split())
        words = words[::-1]
        ans = " ".join(words)

        return ans
