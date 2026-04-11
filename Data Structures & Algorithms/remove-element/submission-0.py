class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
  
        # pointer starts at 0
        # check if nums[i] == to val
            # true? continue
            # false? nums[p] = nums[i]
                # p += 1

        p = 0

        for i in range(len(nums)):
            if (nums[i] != val):
                nums[p] = nums[i]
                p += 1
            else:
                continue
        return p

