# path: leeetcode\python\0066-plus-one.py
# link: https://leetcode.com/problems/plus-one/
# 2023-04-10
# leetcode: Easy

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        one = 1
        i = 0
        digits = digits[::-1]

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(one)
                one = 0
            i += 1
        return digits[::-1]