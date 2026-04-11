class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)
        arr = []

        for n in nums:
            freq[n] += 1
        
        freq_list = sorted(freq.items(), key=lambda item: item[1], reverse=True)

        for i in range(k):
            arr.append(freq_list[i][0])
        return arr