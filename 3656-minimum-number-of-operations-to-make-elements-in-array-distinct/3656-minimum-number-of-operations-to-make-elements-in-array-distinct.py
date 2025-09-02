class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def isDistinct(start):
            distinct = set()
            for n in nums[start:]:
                if n in distinct:
                    return False
                distinct.add(n)
            return True
        
        op = 0
        for i in range(0, len(nums), 3):
            if isDistinct(i):
                return op
            op += 1
        return op

    