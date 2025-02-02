def find_pairs(arr, target):
    seen = set()
    pairs = set()
    
    for num in arr:
        diff = target - num
        if diff in seen:
            pairs.add((min(num, diff), max(num, diff)))
        seen.add(num)
    
    return list(pairs)

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_sum = 10
print(find_pairs(numbers, target_sum))  
# Output: [(1, 9), (2, 8), (3, 7), (4, 6)]
