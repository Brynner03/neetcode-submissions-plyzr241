class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # [1,1,2,3,4]
        #    l
        #      r

           # CHeck if nums[r] == nums[r-1]
            # true? increment r
            
            # false? nums[l] = nums[r]
            # l += 1
            # r += 1
        # return l
        
        l = 1

        for i in range(1, len(nums)):
            if (nums[i] == nums[i-1]):
                continue
            else:
                nums[l] = nums[i]
                l += 1
        
        return l