#1
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1 



#2
class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

#3
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return(-1)
        else:
            return(haystack.find(needle))
