# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # bst all node vals are UNIQUE and p and q, return lowest common ancestor
    # so where one is ancestor of the other, the ancestor is the LCA
    # otherwise, like for one and four LCA is three not five

    # time is O(h), space is O(h), h is height

    # okay so what are my thoughts
    # like a depth first approach, since we can narrow things down quicker with it

    # lets try a first idea
    # so we have the root, ask would p and q be split by it, if so its LCA that was easy
    # or if the root you're looking at is p or q, just return it, that was also easy
    # if p and q don't split it, go down in the direction of p and q

    # does that work? not thinking of any pitfalls
    # tbh i say go for it okay
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # alright so pseudocode time
        # set cur to root ( not really a reason for this lol )
        # do need p to be less than q, so can do if p > q
            # set temp to p, p to q, and q to temp lol, this isn't beautiful but i think
            # the rest is still nice enough to justify it

        # while cur
            # if cur's value is greater than p but less than q, return cur's value
            # if cur's value is p or q, return cur's value
            # if p and q are less than cur's value, set cur to cur.left
            # ow, set cur to cur.right

        # if you get here, well you shouldn't, so error

        cur = root
        l, r = p.val, q.val
        if l > r:
            temp = l
            l = r
            r = temp

        while cur:
            if (l < cur.val and cur.val < r) or (cur.val == l) or (cur.val == r):
                return cur
            elif cur.val > r:
                cur = cur.left
            else:
                cur = cur.right
        
        return None

