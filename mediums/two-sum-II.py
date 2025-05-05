from typing import List


class Solution:

    # okay so two numbers need to sum to target
    # index1 < index2
    # exactly one valid solution
    # O(1) additional space

    # know two pointer problem
    # maybe have index2 start from the right, work its way back
    # then could have index1 check up to where index2 is for the sum
    # wouldn't be fantastic time wise, but good on space

    # could do something similar, but have index1 begin right after index2
    # and also work its way back, don't think this is any better
    # tbh prolly worse time wise

    # what if they both started on the left, obvi would be great for example 1
    # but don't think it stewards time well either lol

    # geez idk about constant time, lets start with the first solution i came
    # up with and go from there


    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # have target
        # have numbers which is a list

        # start index2 at rightmost index equal to or less than target (while loop)
        # start index1 at 0

        # then here need to check if index1 + index2 is target
        # if sum too big, move index2 back
        # if sum too small, move index1 forward
        # if sum correct, yay

        # okay looking at this maybe this is constant time

        # okay i didnt realize it was one indexed that's dumb

        # okay im dumb i didn't consider negative numbers
        # since it includes these, i can't use my cheat 
        # i wonder if i still can and just need to flip the indeces
        # okay nice try

        # okay let's think, so the shortcut i take is def bad so lets cut that
        # lol that solved it i cant i had it from the very beginning and
        # was flying too close to the sun

        index1, index2 = 0, len(numbers) - 1

        sum = numbers[index1] + numbers[index2]

        while sum != target:
            if sum > target:
                index2 -= 1
            else:
                index1 += 1
            sum = numbers[index1] + numbers[index2] 

        return [index1 + 1, index2 + 1]