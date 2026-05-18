class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for i in strs:
            freqs = [0] * 26
            for c in i:
                freqs[ord(c) - ord('a')] += 1
            
            if tuple(freqs) not in map:
                map[tuple(freqs)]= []
            map[tuple(freqs)].append(i)
        
        return list(map.values())
    
        