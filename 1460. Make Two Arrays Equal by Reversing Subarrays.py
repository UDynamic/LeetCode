''' You are given two integer arrays of equal length target and arr.
In one step, you can select any non-empty subarray of arr and reverse it.
You are allowed to make any number of steps.

Return true if you can make arr equal to target or false otherwise.
 

Example 1:

Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true
Explanation: You can follow the next steps to convert arr to target:
1- Reverse subarray [2,4,1], arr becomes [1,4,2,3]
2- Reverse subarray [4,2], arr becomes [1,2,4,3]
3- Reverse subarray [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.
Example 2:

Input: target = [7], arr = [7]
Output: true
Explanation: arr is equal to target without any reverses.
Example 3:

Input: target = [3,7,9], arr = [3,7,11]
Output: false
Explanation: arr does not have value 9 and it can never be converted to target.
 

Constraints:
target.length == arr.length
1 <= target.length <= 1000
1 <= target[i] <= 1000
1 <= arr[i] <= 1000
'''

# Approach 1: Sorting
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        arr.sort()
        target.sort()
        for i in range(len(arr)):
            if arr[i] != target[i]:
                return False
        return True

# Approach 2: Frequency Counting With 2 Dictionaries
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # Dictionary to maintain frequency count for arr
        arrFreq = {}
        for num in arr:
            if num not in arrFreq:
                arrFreq[num] = 1
            else:
                arrFreq[num] += 1

        # Dictionary to maintain frequency count for arr
        targetFreq = {}
        for num in target:
            if num not in targetFreq:
                targetFreq[num] = 1
            else:
                targetFreq[num] += 1

        # Number of distinct elements of the 2 arrays are not equal
        if len(arrFreq) != len(targetFreq):
            return False

        for key in arrFreq:
            # Frequency for num differs
            if arrFreq[key] != targetFreq.get(key, 0):
                return False

        return True


# Approach 3: Frequency Counting With 1 Dictionary
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # Frequency count for arr
        arrFreq = {}
        for num in arr:
            arrFreq[num] = arrFreq.get(num, 0) + 1

        for num in target:
            # If num does not appear in target, then arrays are not equal
            if num not in arrFreq:
                return False

            # Decrement the frequency count for num and
            # remove key if the count goes to 0
            arrFreq[num] -= 1
            if arrFreq[num] == 0:
                del arrFreq[num]
        return len(arrFreq) == 0
