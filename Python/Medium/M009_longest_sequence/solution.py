def longest_consecutive(nums):

    if not nums:
        return 0

    new_nums = sorted(nums)

    longest = 1
    count = 1

    for i in range(len(new_nums) - 1):

        # Skip duplicates
        if new_nums[i] == new_nums[i + 1]:
            continue

        # Consecutive number found
        elif new_nums[i] + 1 == new_nums[i + 1]:
            count += 1

        # Sequence breaks
        else:
            longest = max(count, longest)
            count = 1

    # Final update
    longest = max(longest, count)

    return longest


# Test
nums = [100, 4, 200, 1, 3, 2]

print(longest_consecutive(nums))