#+---------------------------|
# Question
#+---------------------------|

#+---------------------------|
# Solutions
#+---------------------------|
# Approach 1: Greedy Sorting
class Solution:
    def minimumPushes(self, word: str) -> int:
        # Frequency list to store count of each letter
        frequency = [0] * 26

        # Count occurrences of each letter
        for c in word:
            frequency[ord(c) - ord("a")] += 1
        # Sort frequencies in descending order
        frequency.sort(reverse=True)

        total_pushes = 0

        # Calculate total number of presses
        for i in range(26):
            if frequency[i] == 0:
                break
            total_pushes += (i // 8 + 1) * frequency[i]

        return total_pushes

# Approach 2: Using Heap
class Solution:
    def minimumPushes(self, word: str) -> int:
        # Frequency map to store count of each letter
        frequency_map = Counter(word)

        # Priority queue to store frequencies in descending order
        frequency_queue = [-freq for freq in frequency_map.values()]
        heapq.heapify(frequency_queue)

        total_pushes = 0
        index = 0

        # Calculate total number of presses
        while frequency_queue:
            total_pushes += (1 + (index // 8)) * (
                -heapq.heappop(frequency_queue)
            )
            index += 1
        return total_pushes




#+---------------------------|
# Lessons
#+---------------------------|

# ord ():
	# The ord() function in Python 3 is used to return the Unicode code point for a given character. 
	# Essentially, it converts a character into its corresponding integer representation.
'''
Here's a simple example:
# Get the Unicode code point for the character 'A'
unicode_value = ord('A')
print(unicode_value)  # Output: 65

In this example, ord('A') returns 65, which is the Unicode code point for the character 'A'
'''
