def move_zeros(arr):
    non_zeros = [x for x in arr if x != 0]  # Extract non-zero elements
    zeros = [0] * (len(arr) - len(non_zeros))  # Count zeros
    return non_zeros + zeros

# Example usage:
nums = [0, 1, 0, 3, 12]
print(move_zeros(nums))  # Output: [1, 3, 12, 0, 0]
