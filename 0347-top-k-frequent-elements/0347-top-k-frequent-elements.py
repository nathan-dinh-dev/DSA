class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        return [num for num, _ in sorted_items[:k]]