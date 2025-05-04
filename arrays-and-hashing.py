# was using blind 75 roadmap, now moving to neetcode 150 easy to hard since have head knowledge,
# more just need to learn how to think "leetcode"-like

from collections import defaultdict
from typing import List


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

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create output list, could use defaultdict next time to make end cleaner
        output = {}

        # take each item in strs
        for i in strs:
            # get hash array for item to serve as key
            # create 26 size array of 0s
            key = [0] * 26
            for j in i:
                # add to array based on ord
                key[ord(j) - ord('a')] += 1

            # can't hash list bc mutable, cast to tuple
            tuple_key = (tuple(key))

            if tuple_key in output:
                output[tuple_key].append(i)
            else:
                output[tuple_key] = [i]

        return output.values()
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sorting option

        # make a hash map via defaultdict called d with default 0
        d = defaultdict(int)
        for i in nums:
            # += 1 to num's associated key in d
            d[i] += 1

        # take d's values and sort it
        vals = list(zip(d.values(), d.keys()))
        vals.sort()

        # grab the k highest values, return these as the output
        output = []
        while len(output) < k:
            output.append(vals.pop()[1])

        return output

        # above is good on space O(n), time is O(nlogn) 