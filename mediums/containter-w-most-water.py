from typing import List


class Solution:
    # wait okay is this geometry wait it is that's so cool
    # so you have to be smart with it, because the height of 7 would be great, but
    # the width would only allow it to fit 28

    # screams two pointer
    # would probably need to keep track of output the entire time

    # so what would happen if started with l and r (good bc width max)
    # could just move in whichever points to something smaller (or default r idc)

    # trying to think of edge case where this would break bc seems promising, 
    # thought through both on left earlier and didn't work well
    # roxy is barking cant think so just gonna try it, seems solid i hope

    # would also be good runtime and good space
    def maxArea(self, heights: List[int]) -> int:
        # okay so need to start output
        # start l and r at respective spots

        # go while left isnt equal to right (safe bc never double jump)
        # so need to calc width, which would be r - l
        # then need to calc height with whichever is shorter, height at l or r
        # calc output, update output if needed
        # then if r is shorter than l, subtract from r
        # else add one to l

        # return output

        l, r, output = 0, len(heights) - 1, 0

        while l != r:
            width = r - l
            height = min(heights[l], heights[r])

            output = max(width * height, output)
            
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1

        return output