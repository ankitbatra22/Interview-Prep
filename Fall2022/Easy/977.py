class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left_idx, right_idx = 0, len(nums)-1
        output = []
        for i in range(len(nums)):
            if abs(nums[left_idx]) > abs(nums[right_idx]):
                output.append(nums[left_idx] * nums[left_idx])
                left_idx+=1
            else:
                output.append(nums[right_idx] * nums[right_idx])
                right_idx-=1
        return output[::-1]

    # O(n) time, O(n) space