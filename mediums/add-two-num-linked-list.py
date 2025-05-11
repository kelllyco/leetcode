# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:

    # l1 has a linked list of numbers (reverse and concat)
    # l2 has a linked list of numbers (reverse and concat)

    # sum them together, return this as a linked list, put it backwards

    # O(m + n) time, O(1) space

    # okay so first idea...
    # take each list (so one at a time)
    # run through the list, concatting the numbers as a string
    # flip the string using [::-1]
    # and then could do the same thing going backwards after summing

    # above is kinda clunky, but might work

    # is there a cleaner way to do this?
    # ooo wait i think i got it, and it'll def be O(1) space this time instead of idk what

    # okay so run a loop as long as one isnt null
    # take the value you're looking at, sum it, and create a new node with the first digit
    # with a carryover digit, just remember that and add it to the sum of the next one
    # this would be more in place!!
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # okay so now lets write this in more official pseudocode
        # init a carryover var to 0
        # init the head node to the sum linked list
        # while l1 or l2 or carryover != 0
            # sum value of l1 with value of l2 plus carryover
                # l1 and/or l2 might be null at this point, so need to check
            # divide the sum by 10, let this value be the carryover
            # mod the value, let that be the value of the new node
            # make that new node
        # return the head node to the sum list

        carryover = 0
        dummy = ListNode(0)
        cur = dummy

        while l1 or l2 or (carryover != 0):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sumVal = val1 + val2 + carryover
            carryover = sumVal // 10
            toAdd = sumVal % 10

            cur.next = ListNode(toAdd)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

