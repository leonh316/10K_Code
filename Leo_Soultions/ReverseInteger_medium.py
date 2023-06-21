""" 7.Reverse Integer - Medium
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned)."""


# think through the above problem in code steps:
# 1. input a signed 32-bit integer
# 2. reverse the digits of the integer
# 3. if the reversed integer is outside the signed 32-bit integer range, return 0
# 4. else return the reversed integer


# Leo soultion:


i = input("Enter a signed 32-bit integer: ")
print(i)


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