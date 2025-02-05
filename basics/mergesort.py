def mergesort(array):
    if len(array) <= 1:
        return array

    m = len(array) // 2
    left = mergesort(array[:m])
    right = mergesort(array[m:])

    return merge(left, right)


def merge(left, right):
    merged = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    if len(left) > 0:
        merged += left
    else:
        merged += right

    return merged


if __name__ == "__main__":
    input_str = input("Enter numbers, separated by ',': ")

    # Split input string, remove whitespace, and convert to integers
    input_list = [x.strip() for x in input_str.split(",")]
    
    try:
        # Convert to integers
        value_list = [int(x) for x in input_list]
    except ValueError:
        print("Invalid input.")
        quit(1)

    sorted_list = mergesort(value_list)
    print(sorted_list)
