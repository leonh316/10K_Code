""" 7.Reverse Integer - Medium
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned)."""


# think through the above problem in code steps:
# 1. input a signed 32-bit integer
# 2. reverse the digits of the integer
# 3. if the reversed integer is outside the signed 32-bit integer range, return 0
# 4. else return the reversed integer

# Leo soultion:




""" 
# 7.Reverse Integer - Medium - Co-pilot solution

def reverse(x):
    # Reverse the digits of a signed 32-bit integer
    # 1. input a signed 32-bit integer
    # 2. reverse the digits of the integer
    if x >= 0: # if positive
        x = str(x) # convert to string
        x = x[::-1] # reverse the string
        x = int(x) # convert to integer
    else: # if negative
        x = str(x) # convert to string
        x = x[1:] # remove the negative sign
        x = x[::-1] # reverse the string
        x = int(x) # convert to integer
        x = -x # add the negative sign
    # 3. if the reversed integer is outside the signed 32-bit integer range, return 0
    if x < -2**31 or x > 2**31-1:
        return 0
    # 4. else return the reversed integer
    else:
        return x

print() # for testing use


""" 

"""print("1") # for testing use
# 1. input a signed 32-bit integer
x = 123 # input integer here
# 2. reverse the digits of the integer
x = str(x) # convert to string
x = x[::-1] # reverse the string
x = int(x) # convert to integer
# 3. if the reversed integer is outside the signed 32-bit integer range, return 0
str() # convert to string

"""

"""
# Co-pilot solution:

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        if x > 0:
            x = str(x)
            x = x[::-1]
            x = int(x)
            if x > 2**31-1:
                return 0
            else:
                return x
        if x < 0:
            x = str(x)
            x = x[1:]
            x = x[::-1]
            x = int(x)
            if x > 2**31-1:
                return 0
            else:
                return -x
            

# Runtime: 32 ms, faster than 74.93% of Python3 online submissions for Reverse Integer.
# Memory Usage: 14.3 MB, less than 11.15% of Python3 online submissions for Reverse Integer.
"""