class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashMap = {}
        for i in range(1, n + 1):
            key = sum(int(x) for x in str(i))
            if key not in hashMap:
                hashMap[key] = 0
            hashMap[key] += 1

        maxValue = max(hashMap.values())
        count = sum(1 for v in hashMap.values() if v == maxValue)
        return count