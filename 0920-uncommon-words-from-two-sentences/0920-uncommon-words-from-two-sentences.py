class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # words1 = s1.split( ) 
        # words2 = s2.split( )

        # ans = []

        # for i in words1:
        #     if i not in words2 and words1.count(i) == 1:
        #         ans.append(i)
        # for i in words2:
        #     if i not in words1 and words2.count(i) == 1:
        #         ans.append(i)

        # return ans        

        #using counter 

        words = s1.split() + s2.split()

        word_count = Counter(words)
        ans = [word for word, count in word_count.items() if count ==1 ]
        return ans