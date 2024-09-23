class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word_set = set(dictionary)
        l = len(s)

        dp = [0] * (l+1)
        dp[0] = 0

        for i in range(1, l+1):
            dp[i] = dp[i-1] +1
            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])
        
        return dp[l]