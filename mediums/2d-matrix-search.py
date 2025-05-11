from typing import List


class Solution:
    # m x n matrix and int target, rows are increasing as are columns

    # so linearly, seems like you could do bin search with extra math
    # bc like for example 1, matrix is m rows, n columns
    # so 12 is end, minus 1 is 11 since start from 0
    # mid is like 5, which would be // 3 and % 3 which would give row
    # and column, and from there just binary search like normal

    # edge cases where this wouldn't work? idk i think its comprehensive
    # would need to be careful about updating l and r, except not really just 
    # update mid and calc again no crazy conditionals
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # get m as len of matrix
        # get n as len of row of matrix

        # set l to 0, r to m * n minus 1

        # while left is less than right
            # mid is right plus left floor two
            # mid val is matrix[mid // m][mid % m]

            # if target is mid val, return true
            # if target is less than mid val, set r to mid minus 1
            # else, set l to mid plus 1

        # if you get this far, return false
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1

        while l <= r:
            mid = (r + l) // 2
            midVal = matrix[mid // n][mid % n]
            print(midVal)

            if target == midVal:
                return True
            elif midVal > target:
                r = mid - 1
            else:
                l = mid + 1

        return False