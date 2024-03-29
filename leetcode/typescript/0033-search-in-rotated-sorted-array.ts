/**
 * Problem: 33. Search in Rotated Sorted Array
 * Path: leetcode\typescript\0033-search-in-rotated-sorted-array.ts
 * Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
 * Leetcode: Medium
 * Date: 2023-05-10
 */

function search(nums: number[], target: number): number {
  let l: number = 0;
  let r: number = nums.length - 1;

  while (l <= r) {
    let m: number = Math.floor((l + r) / 2);
    if (nums[m] === target) return m;

    if (nums[l] <= nums[m]) {
      if (nums[l] <= target && target <= nums[m]) r = m - 1;
      else l = m + 1;
    } else {
      if (nums[m] <= target && target <= nums[r]) l = m + 1;
      else r = m - 1;
    }
  }
  return -1;
}
