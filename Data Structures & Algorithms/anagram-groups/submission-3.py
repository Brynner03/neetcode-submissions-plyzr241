class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq = defaultdict(list)

        for s in strs:
            curr = defaultdict(int)
            for c in s:
                curr[c] += 1
            cur_tup = tuple(sorted(curr.items()))
            freq[cur_tup].append(s)
        return list(freq.values())