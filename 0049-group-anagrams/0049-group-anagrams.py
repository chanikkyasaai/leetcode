class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ang = defaultdict(list)
        for s in strs:
            ang[''.join(sorted(s))].append(s)
        
        return list(ang.values())