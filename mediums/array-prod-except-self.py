from typing import List


class Solution:
    # okay so have nums, need to return output where its the product of all but i

    # well the division operator would be helpful lol, so something using that is an idea
    # would just muliply everything together, and divide by nums[i] for each
    # output[i]

    # now lets think of another idea
    # making the product one at a time is inefficient
    # well you know it'll require len - 1 inputs each time, could base it off that
    # honestly that might be more efficinet too
    # lets do this so that we dont even need the follow up

    # okay that wasn't going to get me anywhere, prefix suffix technique will!
    # so i go from left to right, make that my prefix array
    # then i go from right to left, make that my suffix array
    # so like for when i is 0, would want right[len(right) - 2] bc don't want very last
    # then for when i is 1, would want left[i + 1] * right[len(right) - 3]
    # and do that til i is done ... maybe set left[0] and right[0] to 1 to avoid issues
    # that logic might be a little off, but the heart is tehre

    # [ 1, 2, 4, 6]

    # [48, 24, 12, 8]

    # left
    # [1, 2, 8, 24]

    # right
    # [6, 24, 48, 48]

    # l- r2
    # l0 r1
    # l1 r0
    # l2 r-

    # so it'd be helpful to do the start of l and r at 1

    # okay so i got it! but turns out the prefix suffix approach wants the 
    # suffix done in the inverse who knew!?

    # also could technically do this in place

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # need to start left at 1 and right at 1, need to have a len of len
        # fill them with 1s, just do 2 for loops for now one through left
        # one through right

        left, right = [1] * len(nums), [1] * len(nums)

        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        output = [0] * len(nums)

        for i in range(len(nums)):
            output[i] = left[i] * right[i]

        return output