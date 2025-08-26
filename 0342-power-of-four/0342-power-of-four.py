class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        val = math.log(n, 4)
        
        return val.is_integer()