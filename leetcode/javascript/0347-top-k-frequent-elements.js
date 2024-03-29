/**
 * Set - Frequency Counter
 * Time O(NlogN) | Space O(N)
 * Path: leetcode\javascript\0347-top-k-frequent-elements.js
 * Link: https://leetcode.com/problems/top-k-frequency-elements/
 * Leetcode: Medium
 * Date: 2023-05-03
 *
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
// var topKFrequent = function (nums, k) {
// 	let frequency = {};
// 	for (let i = 0; i < nums.length; i++) {
// 		if (frequency.hasOwnProperty(nums[i])) frequency[nums[i]] += 1;
// 		else frequency[nums[i]] = 1;
// 	}

// 	let result = Object.keys(frequency).map((key) => [Number(key), frequency[key]]);
// 	let sortedResult = result.sort((a, b) => {
// 		return b[1] - a[1];
// 	});

// 	let output = [];
// 	for (let i = 0; i < k; i++) {
// 		output.push(sortedResult[i][0]);
// 	}

// 	return output;
// };
