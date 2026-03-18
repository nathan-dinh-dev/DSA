class Solution:
    def reverse(self, x: int) -> int:
        MIN_RANGE = -2**31
        MAX_RANGE = 2**31 - 1

        if x < 0:
            sign = -1
        else:
            sign = 1
        
        reverse = 0
        n = abs(x)

        while n:
            remainder = n % 10
            n //= 10
            reverse = reverse * 10 + remainder

        reverse *= sign
        if reverse > MAX_RANGE or reverse < MIN_RANGE:
            return 0
        
        return reverse

                   