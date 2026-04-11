class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq = defaultdict(list)

        for s in strs:
            curr = defaultdict(int)
            for c in s:
                curr[c] += 1
            
            freq_tuple = tuple(sorted(curr.items()))
            freq[freq_tuple].append(s)
        return list(freq.values())