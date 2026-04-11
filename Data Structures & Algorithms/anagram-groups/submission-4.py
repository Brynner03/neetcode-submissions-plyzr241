class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Store the frequency of char to string {(char,count) : [string]}
        freq = defaultdict(list)

        for s in strs:
            # Store the frequency of char in string {char : count}
            cur = defaultdict(int)
            for c in s:
                cur[c] += 1
            # Convert to a tuple because maps cant be keys in Python
            # Sort it 
            tup = tuple(sorted(cur.items()))
            # Append the string to where the char count is in the map
            freq[tup].append(s)

        # Return an array of the strings
        return list(freq.values())