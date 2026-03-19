class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # Sort by the Xend
        points.sort(key=lambda x: x[1])
        arrows = 1
        arrow_x = points[0][1]

        for xStart, xEnd in points[1:]:
            if xStart > arrow_x:
                arrows += 1
                arrow_x = xEnd
        
        return arrows
