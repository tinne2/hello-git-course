def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        mid = len(array) // 2
        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:])
        
        return merge(left, right)

def merge(left, right):
    sorted_list = []
    while left and right:
        if left[0] < right[0]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    sorted_list.extend(left or right)
    return sorted_list

if __name__ == "__main__":
    # Get input list from user
    input_str = input("Enter numbers, separated by ',': ")
    
    # Convert input string to a list of strings (e.g., ['1', '5', '6', ...])
    input_list = input_str.split(',')
    
    # Convert the list of strings to a list of integers (e.g., [1, 5, 6, ...])
    value_list = [int(i) for i in input_list]
    
    # Print the input list (as strings) - exactly as ['1', '5', '6', ...]
    print(f"input_list: {input_list}")
    
    # Print the value list (as integers) - exactly as [1, 5, 6, ...]
    print(f"value_list: {value_list}")
    
    # Perform the merge sort
    sorted_list = merge_sort(value_list)
    
    # Print the sorted array (as final result)
    print(f"array: {sorted_list}")
