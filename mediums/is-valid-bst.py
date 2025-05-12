# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # okay so given a root, true if valid, false if not, pretty clearcut
    # left nodes always have to be less than the key
    # right nodes always have to be greater than the key

    # def depth first search 
    # O(n) time and O(n) space

    # okay a little scared, but i can do this lol
    # so a dfs approach

    # first idea would be preorder transversal
    # okay so look at cur, look left, if greater than, return false
    # otherwise, make left new cur (recursively speaking eek)
    # if no left, check right greater than ( how to make sure its still less than the root if on left side )

    # could do an inorder transversal, and then just make sure that's in ascending order
    # probably a waste time complexity wise

    # hints seem to lean towards original idea, just need to keep track of a tree's lower and 
    # upper limits based on it's subtree ness

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # alright let's walk through the pseudocode

        # def isValid(root, min, max)
            # base case: left and right are None, return true

            # obvi need to check that left and right exist

            # valid bool init it
            # if left less than root val and greater than min
                # valid = isValid(left, min, cur.val)
            # else return false!!!
            # if right greater than root val and less than max
                # valid = isValid(right, cur.val, max)
            # else return false!!!
            # return valid

        # wow i hate recursion okay let's try it

        def isValid(myRoot, myMin, myMax):
            if not myRoot:
                return True
            
            if not (myMin < myRoot.val < myMax):
                return False

            return (isValid(myRoot.left, myMin, myRoot.val) and isValid(myRoot.right, myRoot.val, myMax))

            # messy recursive solution is commented out below, WHICH I DID BY MYSELF
            # AND IT WORKED FIRST TRY, but chat showed me a less psychotic approach
            # valid = True

            # if myRoot.left:
            #     if myRoot.left.val < myRoot.val and myRoot.left.val > myMin:
            #         valid = valid and isValid(myRoot.left, myMin, myRoot.val)
            #     else: 
            #         return False
            # if myRoot.right:
            #     if myRoot.right.val > myRoot.val and myRoot.right.val < myMax:
            #         valid = valid and isValid(myRoot.right, myRoot.val, myMax)
            #     else:
            #         return False
            
            # return valid

        return isValid(root, -1000, 1000)
        