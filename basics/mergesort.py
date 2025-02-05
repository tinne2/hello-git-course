def mergesort(arr):
    print(f"array: {arr}")  # Debugging: showing the array at the current step
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
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
input_list = [int(x) for x in input_str.split(',')]

# Call mergesort on the parsed input list
sorted_list = mergesort(input_list)
print(f"Sorted array: {sorted_list}")
