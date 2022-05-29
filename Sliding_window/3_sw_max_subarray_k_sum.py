# Maximum Sum Subarray of size K | Sliding Window

# arr: Input array
# k: Window size
def max_sum_subarray_sizek(arr: list, k: int):
    """
        Logic is to have i and j point to the two ends of the
        window and sum the elements between them.
        For every iteration,
            subtract the ith index element from the window
            increment both i and j to keep the window size constand;
            Add the jth index element to the window.
    """
    i = j = 0
    max_sum = 0
    window_sum = 0
    # We must process only till we hit the end of array
    while j < len(arr):
        # calculate the sum of window with each iteration
        # add the jth element to the window
        window_sum = window_sum + arr[j]

        # Will the window size is not acheived, just calculate the
        # sum and don't calculate the max.
        if j-i+1 < k:
            j += 1
        elif j-i+1 == k:
            # The elements between i and j are length of one window
            # We must sum them and check if it is greater then the earlier
            # and calculated sum
            max_sum = max(max_sum, window_sum)

            # When we move towards right, we are removing the left element and
            # add right element; Thus we need to remove the a[i] from the window
            # and add a[j] to the window; Addition is performed at begining thus
            # just removing the ith element from window

            window_sum = window_sum - arr[i]
            # For every iteration, we'll increement both i and j to keep the
            # window size constant;
            i += 1
            j += 1
    return max_sum

input_arr = [4, 6, 9, 7, 1, 1, 5, 8]
res = max_sum_subarray_sizek(input_arr, 3)
print(res)

input_arr2 = [3, 5, 1, 7, 2, 7, 9]
res = max_sum_subarray_sizek(input_arr2, 3)
print(res)
