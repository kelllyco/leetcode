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