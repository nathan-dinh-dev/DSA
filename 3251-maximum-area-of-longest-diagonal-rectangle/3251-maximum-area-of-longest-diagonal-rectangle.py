class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxDiagonal, maxArea = 0, 0

        for rect in dimensions:
            diagonal = (rect[0]**2 + rect[1]**2)**0.5
            if maxDiagonal < diagonal:
                maxDiagonal = diagonal
                maxArea = rect[0] * rect[1]
            elif maxDiagonal == diagonal:
                maxArea = max(maxArea, rect[0] * rect[1])
                
        return maxArea