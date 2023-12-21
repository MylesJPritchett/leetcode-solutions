class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_axis = []
        largest_gap = 0
        for point in points:
            x_axis.append(point[0])
        x_axis.sort()
        for i in range(len(x_axis)-1):
            largest_gap = max( x_axis[i+1] - x_axis[i], largest_gap)
        return largest_gap
            