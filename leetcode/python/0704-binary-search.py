# path: leetcode\python\0704-binary-search.py
# link https://leetcode.com/problems/binary-search/
# date 2023-04-07
# leetcode: Easy

from ast import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
         l, r = 0, len(nums) - 1

         while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
         return -1