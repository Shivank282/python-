def has_duplicates(arr):
    return len(arr) != len(set(arr))

# Example usage:
numbers = [1, 2, 3, 4, 5, 3]
print(has_duplicates(numbers))  # Output: True
