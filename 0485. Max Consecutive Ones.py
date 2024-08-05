#+---------------------------|
# Question
#+---------------------------|

#+---------------------------|
# Solutions
#+---------------------------|

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max = cur = 0
        
        for num in nums :
            if num == 0 :
                cur = 0
            else :
                cur += 1
            if cur > max :
                max = cur
        return max
    
Solution = Solution ()
print (Solution.findMaxConsecutiveOnes ([1,1,0,0,1,1,1]))

#+---------------------------|
# Lessons
#+---------------------------|

'''
? why this isn't making " cur " back to 0 when "nums [i]" is equal to 0?

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max = cur = 0
        
        for i in nums :
            if nums [i] == 0 :
                cur = 0
            else :
                cur += 1
            if cur > max :
                max = cur
            print (cur, max)
        return max
        
=>

The issue in your code is with the way you are iterating through the list nums. When you use for i in nums, i takes the value of each element in nums, not the index. Therefore, nums[i] is incorrect because i is already an element of nums, not an index.

You should iterate through the list using an index or directly iterate over the elements. Here's the corrected version of your code:

class Solution:
def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
max_count = cur_count = 0

for num in nums:
if num == 0:
cur_count = 0
else:
cur_count += 1
if cur_count > max_count:
max_count = cur_count
print(cur_count, max_count)

return max_count

In this corrected version:
•  The loop iterates directly over the elements of nums using for num in nums.

•  The variable num represents each element in the list.

•  If num is 0, cur_count is reset to 0.

•  Otherwise, cur_count is incremented by 1.

•  If cur_count exceeds max_count, max_count is updated.

This should work as expected and reset cur_count to 0 whenever an element in nums is 0.

'''
