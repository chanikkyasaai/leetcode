class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = s1.split( ) 
        words2 = s2.split( )

        ans = []

        for i in words1:
            if i not in words2 and words1.count(i) == 1:
                ans.append(i)
        for i in words2:
            if i not in words1 and words2.count(i) == 1:
                ans.append(i)

        return ans        