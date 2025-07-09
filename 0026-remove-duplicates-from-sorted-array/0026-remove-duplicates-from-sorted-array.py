class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicatedSet = set()
        
        indexPos = 0
        
        for i in range(len(nums)):
            if nums[i] not in duplicatedSet:
                duplicatedSet.add(nums[i])
                nums[indexPos] = nums[i]
                indexPos += 1
        
        return indexPos

