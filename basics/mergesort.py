def merge_sort(arr, debug=False):
    # Base case: if the list is of length 1 or less, return it as is
    if len(arr) <= 1:
        return arr

    # Divide the list into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], debug)
    right = merge_sort(arr[mid:], debug)

    # Merge the two sorted halves
    return merge(left, right, debug)

def merge(left, right, debug=False):
    result = []
    i = j = 0

    # Merge the two lists by comparing the elements
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements (if any)
    result.extend(left[i:])
    result.extend(right[j:])

    # Debugging output: Print merge steps (if debug is True)
    if debug:
        print(f"Merging...\nleft: {left}\nright: {right}\nmerged: {result}")

    return result

# Main function to take input and sort the list
if __name__ == "__main__":
    # Get input from user (comma-separated numbers)
    input_list = input("Enter numbers, separated by ',': ").split(',')
    
    # Convert the input to a list of integers
    value_list = [int(x) for x in input_list]

    # Perform merge sort on the list and print the sorted list
    sorted_list = merge_sort(value_list)

    # Print the final sorted list
    print(sorted_list)
