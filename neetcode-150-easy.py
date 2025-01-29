class Solution: 
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hash set solution...
        # vals = set()
        # for i in nums:
        #     if i in vals:
        #         return True
        #     else:
        #         vals.add(i)
        
        # return False

        # best is simpler, hash set length solution...
        return len(set(nums)) < len(nums)

    def isAnagram(self, s: str, t: str) -> bool:
        # sorting solution...
        # if len(s) != len(t):
        #     return False

        # return sorted(s) == sorted(t)

        # optimized hash table solution...
        # auto false, don't bother wasting time
        if len(s) != len(t):
            return False

        # array filled w 0s for each letter
        count = [0] * 26

        # run through length of word
        for i in range(len(s)):
            # if the letter is in s, add 1 to its associated array index
            count[ord(s[i]) - ord('a')] += 1
            # if the letter is in t, sub ''
            count[ord(t[i]) - ord('a')] -= 1

        # run through each letter in the array
        for val in count:
            # if a value isnt zero (matched amnt in s/t, return False)
            if val != 0:
                return False
        return True

    def isPalindrome(self, s: str) -> bool:
        # could sort and make sure each char num is even
        # bad bc time expensive

        # two pointers seems good, one at the back and one at the front
        # increment/decrement by 1 each time, making sure pointing to the same thing
        # do this until the pointer pointer right is not greater than pointer left
        # if ever don't point to the same, return false
        # else return true

        # does need to be case insensitive, turn s to lower first
        # also need to strip of non alphanumeric

        # two pointers space is good, no duplicating, so O(n)
        # time looks good too O(n)

        # had thought to clean string like this, but makes space complexity linear
        # s = s.lower()
        # s = re.sub(r'[^a-zA-Z0-9]','', s)

        # account for alphanumeric req in place instead
        
        l = 0
        r = len(s) - 1

        while (l < r):
            while (l < r) and not s[l].isalnum():
                l += 1
            while (l < r) and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True
    
    def maxProfit(self, prices: List[int]) -> int:
        # wrote ideas in navy notebook

        # so idea is have pointer, slice prices based off ptr and run max
        # will just need a profit holder, fill w max - *ptr if its bigger than val cur
        # in profit

        # bad idea, this is still O(n^2) bc of the slicing

        # forgot that if r is less than l, l is obvi not going to be the best
        # time to buy and can just move on...if r is always less than l there
        # is no good time to buy

        # need l = 0 and r = 1
        # profit = 0
        # while r < len(prices) 
            # if l > r
                # if r - l > profit
                    # profit = r - l
            # else 
                # l += 1
        
            # r += 1
        # return profit

        l = 0
        r = 1
        profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                if (prices[r] - prices[l]) > profit:
                    profit = prices[r] - prices[l]
            else:
                l = r
            r += 1
        return profit
    

    def isValid(self, s: str) -> bool:
        # have a filo stack that's empty
        # if s[i] is open, push onto stack
        # if s[i] is closed, pop from stack...if pop doesn't match false
        # if s[i] is closed while stack is empty...false

        # if s runs out while stuff is still in stack, false
        stack = []
        for c in s:
            if c == "[" or c == "{" or c == "(":
                stack.append(c)
            else:
                if not stack:
                    return False
                temp = stack.pop()

                if temp == "[" and c != "]":
                    return False
                if temp == "{" and c != "}":
                    return False
                if temp == "(" and c != ")":
                    return False
        if not stack:
            return True
        return False
    

    def search(self, nums: List[int], target: int) -> int:
        # binary search attempt for the first time in a year and a half lol
        # remember lots of dividing by two and midpoint
        # time is O(logn) which is binary search, space O(1)

        # cant do recursion bc call stack with space
        # need to do iterative solution

        # so have a while loop

        # have target
        # have high, low, mid

        high = len(nums)
        low = 0

        while high > low:
            mid = ((high - low) // 2) + low

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid

        return -1

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # okay so need O(n) time, O(1) space
        # aka linear time and in place

        # so basically need to change where next points for everything
        # going to just rotate through prev, curr, and next

        # originally used temp, but there were weird edge cases i was having
        # to account for...now using temp based off of soulution provided
        # my answer was still O(n) and in place tho :)
        prev = None
        curr = head

        while curr:
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp 
        return prev

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # okay so O(m + n) time and O(1) space

        # should have two ptrs, l1 and l2
        # point them both at the front of list1 and list2, respectively

        # while l1 or l2
        # get the vals of l1 and l2 (obvi one could be None)
        # pick the smaller one, make it output.next and the new tail of output

        # return output

        # my solution is below, worked and met time and space complexity but 
        # could have been less convoluted...better solution uncommented

        # l1, l2 = list1, list2
        # head, lstPtr = None, None

        # while l1 or l2:
        #     temp = None
        #     if not l1:
        #         temp = l2
        #         l2 = l2.next
        #     elif not l2:
        #         temp = l1
        #         l1 = l1.next
        #     elif l1.val <= l2.val:
        #         temp = l1
        #         l1 = l1.next
        #     else:
        #         temp = l2 
        #         l2 = l2.next

        #     if not head:
        #         head = temp
        #         lstPtr = head
        #     else:
        #         lstPtr.next = temp
        #         lstPtr = temp

        # return head

        temp = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return temp.next

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # okay so gonna place the root in a queue (fifo)

        # then take the first item in the queue, swap the left and right nodes, then push
        # both back into the queue, the new left going first

        if not root:
            return root

        queue = [root]

        while queue:
            node = queue.pop(0)

            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root

