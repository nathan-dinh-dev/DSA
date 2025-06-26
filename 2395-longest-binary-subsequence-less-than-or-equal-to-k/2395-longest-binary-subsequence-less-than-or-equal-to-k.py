class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        
        count = 0

        current_sum = 0

        for index, char in enumerate(s[::-1]):
            if char == '0':
                count += 1
            else:
                if (2**index + current_sum) <= k:
                    count += 1
                    current_sum += 2**index
                else:
                    continue
        
        return count
