class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) <3:
            return []
        nums.sort()
        result, N = [], len(nums)
        for i in range(N-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            s, e = i + 1, N-1
            while s < e:
                if nums[s] + nums[e] == -nums[i]:
                    result.append([nums[i], nums[s], nums[e]])
                    s += 1
                    e -= 1
                    while s < e and nums[s] == nums[s-1]:
                        s += 1
                    while s < e and nums[e] == nums[e+1]:
                        e -= 1
                elif nums[s] + nums[e] < -nums[i]:
                    s += 1
                elif nums[s] + nums[e] > -nums[i]:
                    e -= 1
        return result

# Runtime: O(n^2)
# Space: O(n)
