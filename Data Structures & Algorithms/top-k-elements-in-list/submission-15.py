class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        my_map = defaultdict(int)
        freq = []

        for n in nums:
            my_map[n] += 1

        sorted_arr = dict(sorted(my_map.items(), key=lambda item: item[1], reverse=True))
        
        for key, value in sorted_arr.items():
            if k > 0:
                freq.append(key)
                k -= 1
        
        return freq