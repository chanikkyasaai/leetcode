class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        ans = [0] * len(words)

        prefixscore = {}

        for word in words:
            for i in range(1,len(word)+1):
                if word[:i] in prefixscore:
                    prefixscore[word[:i]] +=1
                else:
                    prefixscore[word[:i]] =1

        for i,word in enumerate(words):
            for j in range(1,len(word)+1):
                ans[i]+= prefixscore[word[:j]]

        
        return ans
