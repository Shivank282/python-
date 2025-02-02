def second_largest(arr):
    unique_numbers = list(set(arr))  # Remove duplicates
    if len(unique_numbers) < 2:
        return None  # No second largest
    unique_numbers.sort(reverse=True)  
    return unique_numbers[1]

# Example usage:
numbers = [10, 20, 4, 45, 99, 99]
print(second_largest(numbers))  # Output: 45
