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
    
    # Convert input string to a list of numbers
    input_list = input_str.split(',')
    value_list = [int(i) for i in input_list]
    
    print(f"input_list: {input_list}")
    print(f"value_list: {value_list}")
    
    # Perform the merge sort
    sorted_list = merge_sort(value_list)
    
    # Print the sorted array
    print(f"array: {sorted_list}")
