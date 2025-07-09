class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        indexPos = 1

        count = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 0

            if count < 2:
                nums[indexPos] = nums[i]
                indexPos += 1

        return indexPos            