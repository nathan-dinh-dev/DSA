class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        max_diff = -1
        min = nums[0]

        for i in range (1, len(nums)):
            if nums[i] > min:
                max_diff = max(max_diff, nums[i] - min)
            else:
                min = nums[i]

        return max_diff 