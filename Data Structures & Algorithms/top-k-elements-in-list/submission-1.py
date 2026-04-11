class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1
        
        freq_list = sorted(freq.items(), key=lambda item: item[1], reverse=True)

        arr = [freq_list[i][0] for i in range(k)]
        return arr