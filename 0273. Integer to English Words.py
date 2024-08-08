#+---------------------------|
# Question
#+---------------------------|
'''
Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 

Constraints:

0 <= num <= 231 - 1
'''
#+---------------------------|
# Solutions
#+---------------------------|

# Approach 1: Recursive Approach
class Solution:
    # Arrays to store words for numbers less than 10, 20, and 100
    below_ten = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    below_twenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    below_hundred = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    # Main function to convert a number to English words
    def numberToWords(self, num: int) -> str:
        # Handle the special case where the number is zero
        if num == 0:
            return "Zero"
        # Call the helper function to start the conversion
        return self._convert_to_words(num)

    # Recursive function to convert numbers to words
    # Handles numbers based on their ranges: <10, <20, <100, <1000, <1000000, <1000000000, and >=1000000000
    def _convert_to_words(self, num: int) -> str:
        if num < 10:
            return self.below_ten[num]
        if num < 20:
            return self.below_twenty[num - 10]
        if num < 100:
            return self.below_hundred[num // 10] + (" " + self._convert_to_words(num % 10) if num % 10 != 0 else "")
        if num < 1000:
            return self._convert_to_words(num // 100) + " Hundred" + (" " + self._convert_to_words(num % 100) if num % 100 != 0 else "")
        if num < 1000000:
            return self._convert_to_words(num // 1000) + " Thousand" + (" " + self._convert_to_words(num % 1000) if num % 1000 != 0 else "")
        if num < 1000000000:
            return self._convert_to_words(num // 1000000) + " Million" + (" " + self._convert_to_words(num % 1000000) if num % 1000000 != 0 else "")
        return self._convert_to_words(num // 1000000000) + " Billion" + (" " + self._convert_to_words(num % 1000000000) if num % 1000000000 != 0 else "")


# Approach 2: Iterative Approach
class Solution:
    def numberToWords(self, num: int) -> str:
        # Handle the special case where the number is zero
        if num == 0:
            return "Zero"

        # Arrays to store words for single digits, tens, and thousands
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        # StringBuilder to accumulate the result
        result = ""
        # each chunk of three digits from far right
        group_index = 0

        # Process the number in chunks of 1000 (e.g. chunks of three digits)
        while num > 0:
            # Process the last three digits 
            if num % 1000 != 0: # else is either 0 meaning all the chunks have been processed or a number representing next chunks
                group_result = ""
                part = num % 1000
                    # 655 % 1000 = 655
                    # 1655 % 1000 = 655
                    # 1654655 % 1000 = 655

                # Handle hundreds
                if part >= 100:
                    group_result += ones[part // 100] + " Hundred "
                    part %= 100

                # Handle tens and units
                if part >= 20:
                    group_result += tens[part // 10] + " "
                    part %= 10

                # Handle units
                if part > 0:
                    group_result += ones[part] + " "

                # Append the scale (thousand, million, billion) for the current group
                group_result += thousands[group_index] + " "
                # Insert the group result at the beginning of the final result
                result = group_result + result
            # Move to the next chunk of 1000
            num //= 1000
            group_index += 1

        return result.strip()
 
# Approach 3: Pair-Based Approach
class Solution:
    # Dictionary to store words for numbers
    number_to_words_map = {
        1000000000: "Billion",
        1000000: "Million",
        1000: "Thousand",
        100: "Hundred",
        90: "Ninety",
        80: "Eighty",
        70: "Seventy",
        60: "Sixty",
        50: "Fifty",
        40: "Forty",
        30: "Thirty",
        20: "Twenty",
        19: "Nineteen",
        18: "Eighteen",
        17: "Seventeen",
        16: "Sixteen",
        15: "Fifteen",
        14: "Fourteen",
        13: "Thirteen",
        12: "Twelve",
        11: "Eleven",
        10: "Ten",
        9: "Nine",
        8: "Eight",
        7: "Seven",
        6: "Six",
        5: "Five",
        4: "Four",
        3: "Three",
        2: "Two",
        1: "One"}

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        for value, word in self.number_to_words_map.items():
            # Check if the number is greater than or equal to the current unit
            if num >= value:
                # Convert the quotient to words if the current unit is 100 or greater
                prefix = (self.numberToWords(num // value) + " ") if num >= 100 else ""

                # Get the word for the current unit
                unit = word

                # Convert the remainder to words if it's not zero
                suffix = "" if num % value == 0 else " " + self.numberToWords(num % value)

                return prefix + unit + suffix

        return ""

#+---------------------------|
# Lessons
#+---------------------------|

# another way of writing "if statement":
    # self._convert_to_words(num % 10) if num % 10 != 0 else ""
'''
* Ternary Conditional Operator:
result = self._convert_to_words(num % 10) if num % 10 != 0 else ""

* Equivalent if Statement:
if num % 10 != 0:
result = self._convert_to_words(num % 10)
else:
result = ""
'''
