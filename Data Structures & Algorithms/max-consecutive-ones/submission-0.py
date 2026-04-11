class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        currCount = 0
        maxCount = 0

        for num in nums:
            if num == 1:
                currCount += 1
            else:
                currCount = 0
            maxCount = max(currCount, maxCount)
        
        return maxCount