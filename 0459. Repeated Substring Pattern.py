#+---------------------------|
# Question
#+---------------------------|
'''
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
'''

#+---------------------------|
# Solutions
#+---------------------------|

# My solution
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        cur = ""
        lenLimit = len (s) / 2
        is_repeatable = False
        
        for Char in s:    
            cur = cur + Char
            remain = len (s) % len (cur)
            dev = len (s) // len (cur)
            
            if len (cur) > lenLimit :
                return is_repeatable
            
            if remain != 0 :
                continue
            elif s == (cur * dev) :
                is_repeatable = True
            
            
        return is_repeatable
            
            
# 2
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n//2 + 1):
            if n % i == 0:
                substring = s[:i]
                if substring * (n // i) == s:
                    return True
        return False
    
# 3
# !? what is it ?!
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]
#+---------------------------|
# Lessons
#+---------------------------|
'''
This is an elegant and concise solution to check if a given string can be constructed by repeating a substring. Let's break down how it works:

Explanation
1. 
Concatenation: The expression (s + s) creates a new string by concatenating the original string s with itself. For example, if s = "abc", then (s + s) = "abcabc".
2. 
Slicing: The slice [1:-1] removes the first and the last character of the concatenated string. For s = "abc", (s + s)[1:-1] results in "bcabca".
3. 
Membership Check: The expression s in (s + s)[1:-1] checks if the original string s is a substring of the sliced string. If s can be constructed by repeating a substring, it will appear in this sliced version.

Example
Let's see how this works with an example:

•  For s = "abab":

•  (s + s) = "abababab"

•  (s + s)[1:-1] = "bababab"

•  Since "abab" is a substring of "bababab", the function returns True.

•  For s = "abcabc":

•  (s + s) = "abcabcabcabc"

•  (s + s)[1:-1] = "bcabcabcab"

•  Since "abcabc" is a substring of "bcabcabcab", the function returns True.

•  For s = "abcd":

•  (s + s) = "abcdabcd"

•  (s + s)[1:-1] = "bcdabc"

•  Since "abcd" is not a substring of "bcdabc", the function returns False.

Full Code
Here's the complete code for the solution:

class Solution:
def repeatedSubstringPattern(self, s: str) -> bool:
return s in (s + s)[1:-1]

This approach is efficient and leverages string operations to determine if the string can be formed by repeating a substring.
'''
