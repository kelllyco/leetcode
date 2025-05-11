from typing import List


class Solution:
    # all elements are unique
    # needs to run on O(log n) time, that runtime makes me lean binary search

    # array was in ascending order, so from smallest to largest
    # okay just need to return the minimum number in the array

    # tough bc not 'sorted', basically need to find where going left one
    # increases instead of decreases

    # so maybe a 'modified' binary search
    # so if midpoint is greater than left but less than right, the break
    # must be to the right, so replace left with midpoint

    # using min would be duh, but that's O(n)
    def findMin(self, nums: List[int]) -> int:
        # so need to start left at 0, right at length of nums

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] > nums[r]:
                l = mid + 1

            else:
                r = mid

        return nums[l]