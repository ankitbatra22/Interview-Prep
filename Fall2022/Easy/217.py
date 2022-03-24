class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap:
                return True
            else:
                hashMap[nums[i]] = i
        return False

#gg ez
# O(n) time and O(1) space
# Could also do return len(set(nums)) != len(nums)

