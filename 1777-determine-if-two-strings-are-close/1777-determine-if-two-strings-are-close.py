class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        chardict = {}
        for i in word1:
            if i in chardict:
                chardict[i]+=1
            else:
                chardict[i] = 1
        l1 = sorted(list(chardict.values()))
        c1 = sorted(list(chardict.keys()))
        
        chardict2 = {}
        for i in word2:
            if i in chardict2:
                chardict2[i]+=1
            else:
                chardict2[i] = 1
        l2 = sorted(list(chardict2.values()))
        c2 = sorted(list(chardict2.keys()))

        return l1==l2 and c1==c2
        
