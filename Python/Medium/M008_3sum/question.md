15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that:
- i != j, i != k, and j != k
- nums[i] + nums[j] + nums[k] == 0

The solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Explanation:
(-1) + 0 + 1 = 0
0 + 1 + (-1) = 0
(-1) + 2 + (-1) = 0

Distinct triplets are [-1,0,1] and [-1,-1,2].