class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)
        answer = []

        for num in nums:
            freq[num] += 1
        
        freq_list = sorted(list(freq.items()), key=lambda x: x[1])

        top_tuples = freq_list[-k:]

        for num, freq in top_tuples:
            answer.append(num)

        return answer