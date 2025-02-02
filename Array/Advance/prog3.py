def longest_consecutive_sequence(arr):
    num_set = set(arr)
    max_length = 0

    for num in num_set:
        if num - 1 not in num_set:  # Start of a sequence
            current_num = num
            length = 1

            while current_num + 1 in num_set:
                current_num += 1
                length += 1

            max_length = max(max_length, length)

    return max_length

# Example usage:
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_sequence(nums))  # Output: 4 (Sequence: [1, 2, 3, 4])
