class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Use a map to store frequency of each number
        # Loop through map to check if it appears >= k
            # True: Add it to a separate array
        # Return array

        my_map = defaultdict(int)
        freq = []

        for n in nums:
            my_map[n] += 1

        sorted_map = dict(sorted(my_map.items(), key=lambda item: item[1], reverse=True))
        
        for key, value in sorted_map.items():
            if k > 0:
                freq.append(key)
                k -= 1
        
        return freq