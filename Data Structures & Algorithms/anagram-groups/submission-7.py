class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sorted_map = defaultdict(list)

        for string in strs:
            sorted_string = ''.join(sorted(string))
            sorted_map[sorted_string].append(string)
        output = list(sorted_map.values())
        return output