
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