class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diff_map = defaultdict(int)

        for i, n in enumerate(nums):
            diff = target - n 
            if n in diff_map:
                return [diff_map[n], i]
            else:
                diff_map[diff] = i
        return []