def mergesort(arr):
    print(f"array: {arr}")  # Debugging: showing the array at the current step
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    print(f"m: {mid}")  # Debugging: show the midpoint
    left_half = mergesort(arr[:mid])  # Recursively sort the left half
    right_half = mergesort(arr[mid:])  # Recursively sort the right half
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    print(f"Merging...\nleft: {left}\nright: {right}")  # Debugging: showing left and right arrays to merge
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    print(f"merged: {result}")  # Debugging: showing the merged array
    return result

# Input parsing: change input format as needed
input_str = input("Enter numbers, separated by ',': ")
# Strip spaces from the input values
input_list = [int(x.strip()) for x in input_str.split(',')]

# Debugging: Print the input list without spaces after commas
print(f"input_list: {[x.strip() for x in input_str.split(',')]}")
# Print the value list without spaces after commas
print(f"value_list: {str(input_list).replace(', ', ',')}")

# Call mergesort on the parsed input list
sorted_list = mergesort(input_list)
# Print the final sorted array without the prefix
print(sorted_list)
