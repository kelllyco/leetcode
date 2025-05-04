from typing import List


class Solution:

    # thought is to \n between everything
    # or something of the sort

    # maybe could hash everything, since would know the length
    # not super efficient for space though, or time really

    # really think delimiter is the way to go 

    # okay let's try it and see how it goes

    # okay so similar to that, kinda like with padding, gonna do 
    # the length, followed by #, then the str

    # all this can be prepended, so it's not like you'd accidentally run into
    # the string itself

    def encode(self, strs: List[str]) -> str:
        # okay so im going to take the len of strs[i]
        # think itd be best to do a for loop through m and then
        # take the length, reassign to strs[i]
        # then after the loop smush it together and return

        # chat says dont do in place next time, could just do [(str(len(s)) + '#' + s) for s in strs]
        for i in range(len(strs)):
            strs[i] = (str)(len(strs[i])) + '#' + strs[i]

        return ''.join(strs)

    def decode(self, s: str) -> List[str]:
        # then here could just do a for loop through the input s
        # indexing based on the little number guy
        # while loop might be easier with all the jumping, for would
        # give anyone reading a headache
        max_len = len(s)
        to_jump = ""
        str_list = []
        i = 0

        # so for the while loop itself, will have it run based off len
        # to avoid having to use breaks
        while i < max_len:
            # options in here will be if pointing to a #, jump i forward
            # based on how long the thing you have in num is ... cast that
            # to an int for the jump, and then clear it out

            # okay forgot to put the variable in a list lol, so do that too
            if s[i] == '#':
                i += 1
                int_to_jump = (int)(to_jump)
                to_jump = ""
                str_list.append(s[i: i + int_to_jump])
                i += int_to_jump
            else:
                to_jump += s[i]
                i += 1


            # ow, its a number, and concat to the number str holder
            
        return str_list
