"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: We have to calculate sides of land shared with water which is 16 here.


"""
class Solution:            
    def landSides(self, grid, i, j, r, c):
        
        moves = [(1,0), (0,1), (-1, 0), (0, -1)]
        ans = 0
        
        for move in moves:
            x, y = i + move[0], j + move[1]
            if 0 <= x < r and 0 <= y < c and grid[x][y] == 1:
                ans += 1
        return ans
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        r = len(grid)
        c = len(grid[0])
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    ans += 4 - self.landSides(grid, i, j, r, c)
        return ans
