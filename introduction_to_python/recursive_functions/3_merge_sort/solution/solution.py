def custom_sort(num_list):
    if len(num_list) > 1:
        mid = len(num_list) // 2
        left = num_list[:mid]
        right = num_list[mid:]

        # Recursive call on each half
        custom_sort(left)
        custom_sort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              num_list[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                num_list[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            num_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            num_list[k]=right[j]
            j += 1
            k += 1
    return num_list