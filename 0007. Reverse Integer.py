#+---------------------------|
''' Question
#+---------------------------|
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
'''
#+---------------------------|
# Solutions
#+---------------------------|

''' Solution 1 - Convert to string
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        if x < 0:
            res = int(str(x)[1:][::-1]) * -1
        else:
            res = int(str(x)[::-1])
        
        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0
        
        return res
'''
''' Solution 2 - Using remainder
class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False

        if x < 0:
            is_negative = True
            x *= -1
        
        res = 0
        while x > 0:
            res = (res * 10) + (x % 10)
            x //= 10
        
        if res > 2 ** 31 - 1:
            return 0
        
        return res * -1 if is_negative else res
'''

''' Solution 3
class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            is_negative = True
            x *= -1

        res = 0
        while x > 0:
            digit = x % 10
            x //= 10
            if (res > (2 ** 31 - 1) // 10) or (res == (2 ** 31 - 1) // 10 and digit > 7):
                return 0
            res = (res * 10) + digit

        return -res if is_negative else res
'''
#+---------------------------|
# Lessons
#+---------------------------|
