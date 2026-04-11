class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = defaultdict(int)
        return_arr = []

        for num in nums:
            freq_map[num] += 1
        
        sorted_list = sorted(freq_map.items(), key=lambda item: item[1], reverse=True)

        for i in range(k):
            return_arr.append(sorted_list[i][0])
        
        return return_arr