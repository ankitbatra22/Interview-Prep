class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        if len(nums) != 0:
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[pos], nums[i] = nums[i], nums[pos]
                    pos+=1

    # O(n) time, O(1) space
    