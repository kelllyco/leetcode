from typing import List


class Solution:
    # okay so i have a grid that's two dimensional
    # oo okay im allowed O(m * n) space thank goodness
    
    # first thought is to make a copy of the grid with all 0s, 1s will represent checked
    # gotta use recursion here i think
    # so i could do a search funciton that checks up right down left, and keeps track
    # of count, if finds a one calls the search funciton on that one too
    # don't call if already been checked based on the copy

    # this would be a dfs, tbh im not really positive of another way
    def numIslands(self, grid: List[List[str]]) -> int:
        # so make searched, fill an i by j grid with 0s

        # count is 0

        # lets just start with the recursive function lol
        # for row in grid
            # for col in row
                # if not searched, call search
                # add result of search to count

        # return count

        # def search(i, j):
            # mark i, j as searched in copy
            # if grid at i, j is an island
                # search up (if can)
                # search down (if can)
                # search left (if can)
                # search right (if can)
                # return 1
            # else return 0

        i, j = len(grid), len(grid[0])
        searched = []
        for _ in range(len(grid)):
            row = []
            for _ in range(j):
                row.append(0)
            searched.append(row)
        
        count = 0

        # funciton will assume valid indeces passed in
        def search(x, y):
            if searched[x][y] == 1:
                return 0
            
            searched[x][y] = 1

            if grid[x][y] == "1":
                if y < j - 1:
                    search(x, y + 1)
                if x < i - 1:
                    search(x + 1, y)
                if y > 0:
                    search(x, y - 1)
                if x > 0:
                    search(x - 1, y)
                return 1
            return 0

        for I in range(i):
            for J in range(j):
                count += search(I, J)

        
        return count


