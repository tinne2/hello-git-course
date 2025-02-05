def merge_sort(arr):
    if len(arr) > 1:
        # Print the current state of the array
        print(f"array: {arr}")
        
        # Find the middle of the array
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursively split the array
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        
        # Merge the left and right halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Check if any element was left in the left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        # Check if any element was left in the right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
        
        # Print the merged array after each step
        print(f"Merging...\nleft: {left_half}\nright: {right_half}\nmerged: {arr}")

# Main function to run the program
if __name__ == "__main__":
    # Get the input list from the user
    input_str = input("Enter numbers, separated by ',': ")
    input_list = [x.strip() for x in input_str.split(',')]
    
    # Convert the input to integers
    value_list = [int(x) for x in input_list]
    
    # Print the initial input
    print(f"input_list: {input_list}")
    print(f"value_list: {value_list}")
    
    # Sort the list using merge_sort
    merge_sort(value_list)
    
    # Print the final sorted array
    print(f"Sorted array: {value_list}")
