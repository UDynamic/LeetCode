#+---------------------------|
# Question
#+---------------------------|

#+---------------------------|
# Solutions
#+---------------------------|
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fin = []
        C0 = 0
        for num in nums :
            if num != 0 :
                fin.append (num)
            else :
                C0 +=1
        c = [0] * C0
        nums = fin + c
        return nums
        
A = Solution ()
print (A.moveZeroes([0,1,0,3,12]))


# The script is correct but it doesn't approve because it's not modifying nums in-place
# => Correction:
class Solution:
    def move_zeroes(self, nums: list[int]) -> None:
        # Position to place the next non-zero element 
        # or the left pointer
        pos = 0  
        for i in range(len(nums)):
            # i is the right pointer
            if nums[i] != 0:
                nums [pos], nums [i] = nums [i], nums [pos]
                pos += 1

B = Solution ()
print (B.move_zeroes ([0,1,0,3,12]))
#+---------------------------|
# Lessons
#+---------------------------|
