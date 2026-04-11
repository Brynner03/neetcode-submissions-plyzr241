class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq = defaultdict(list)

        for s in strs:
            curr_freq = defaultdict(int)
            for c in s:
                curr_freq[c] += 1
            
            freq_tuple = tuple(sorted(curr_freq.items()))
            freq[freq_tuple].append(s)
        
        return list(freq.values())