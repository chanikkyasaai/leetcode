class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            
            node = node.children[char]
            node.count+=1
    
    def search(self, word):
        node = self.root
        score = 0

        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
            score+= node.count
        
        return score


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        # ans = [0] * len(words)

        # prefixscore = {}

        # for word in words:
        #     for i in range(1,len(word)+1):
        #         if word[:i] in prefixscore:
        #             prefixscore[word[:i]] +=1
        #         else:
        #             prefixscore[word[:i]] =1

        # for i,word in enumerate(words):
        #     for j in range(1,len(word)+1):
        #         ans[i]+= prefixscore[word[:j]]

        
        # return ans

        trie = Trie()
        for word in words:
            trie.insert(word)
        
        return [trie.search(word) for word in words]

