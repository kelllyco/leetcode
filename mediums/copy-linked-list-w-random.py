
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # random is truly random, can be null, multiple to the same, or to self
    # 0 indexed

    # need to deep copy the linked list with a random pointer
    # the random pointer definetly complicates things, since head might point
    # to something at the very end which is annoying

    # okay so let's think through this
    # one thought could be start at the head, set the value and the next 
    # and if can't do random yet, point it to null and add the pointer to that node
    # and the value of the random node in a list tuple
    # then once im all the way through, go through that list/queue, when looking at 7
    # point it to 5, and pop that
    # you would also need to store the pointers, this isn't great


    # actually i think that's the right track, let's just simplify a bit
    # well could just run through the og linked list twice, the first time doing
    # the copy, the second time dealing with the pointers

    # that would be O(n) time and O(n) space so its what we're looking for
    # okay let's go this way and break it down further
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # init a new head, call it copy
        # while headptr.next (of og) isn't null
            # headptr's value to copyptr's value
            # copyptr's random to null
            # if headptr's next is null set copyptr's next to null
            # ow set copyptr's next to a new node

            # what if in here, took headptr's random's value, and stored
            # the value of headptr and the value of random in a queue of lists


        # now reset the headptr and copyptr and start again

        # okay was close, but was missing the hash map (watched the video)
        oldToCopy = { None : None} # hash map, if its null point it to null

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy # map old node to copy node
            cur = cur.next

        cur = head

        # set the pointers
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]