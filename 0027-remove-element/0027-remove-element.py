class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        indexPOS = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[indexPOS] = nums[i]
                indexPOS += 1
        
        return indexPOS