'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], 
then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Constraints:
  -2^31 <= x <= 2^31 - 1
'''

#CODE

class Solution:
    def reverse(self, x: int) -> int:
        Max = pow(2,31)-1
        Min = -(pow(2,31))
        ans = 0
        n = x
        if x < 0:
            x = abs(x)
        while(x != 0):
            rem = x%10
            ans = (ans*10)+rem
            x = x//10
        if ans >= Max:
            return 0
        elif n > 0:
            return ans
        else:
            return -ans
        
