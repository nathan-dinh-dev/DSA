class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        biggest = num_str
        pos = 0

        while pos < len(num_str) and num_str[pos] == "9":
            pos += 1

        if pos < len(num_str):
            biggest = biggest.replace(biggest[pos], "9")
        num_str = num_str.replace(num_str[0], "0")

        return int(biggest) - int(num_str)
        
        