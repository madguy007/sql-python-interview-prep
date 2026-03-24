# Approach 1: Brute Force (O(n^3))
class Solution(object):
    def threeSum(self, nums):
        result = []

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in result:
                            result.append(triplet)

        return result


# Approach 2: Using Set to Remove Duplicates (Your Version)
class Solution(object):
    def threeSum(self, nums):
        result = []

        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append(sorted([nums[i], nums[j], nums[k]]))

        # Remove duplicates using set
        unique = [list(x) for x in set(tuple(x) for x in result)]
        return unique


# Approach 3: Optimized Two Pointer (Best Approach - O(n^2))
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums)):
            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # Skip duplicates for j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicates for k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return result