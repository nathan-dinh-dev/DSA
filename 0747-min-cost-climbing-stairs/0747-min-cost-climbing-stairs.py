class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        minimum_cost = [0 for _ in range(len(cost) + 1)]

        for i in range(2, len(cost) + 1):
            take_one_step = minimum_cost[i-1] + cost[i-1]
            take_two_step = minimum_cost[i-2] + cost[i-2]
            minimum_cost[i] = min(take_two_step, take_one_step)
        
        return minimum_cost[i]