import logging
logging.basicConfig(level=logging.INFO)

def first_one_in_infinity_sorted_binary_array(arr):
    """
    Find the first 1 in sorted binary array
    Logic:
        For infinity binary sorted array, we can't apply BS as we don't have
        high index.
        We'll check the range in which first 1 could be found by increasing
        the range by 2 for every cycle.

        Once we find the range, we need to apply BS such that
            if a[mid-1] == 0 and a[mid] == 1:
                return the index
            else if current index is 0:
                move to right array
            else: move to left array
    """
    # This is required if the array have only one index, which would be incorrect
    # as per problem statement, but still its good to have a sanity check.
    if arr[0] == 1:
        return 0

    # Try to find the range in which item could be found
    low = 0
    high = 1
    while arr[high] != 1:
        logging.debug('current middle = %s', arr[high])
        # for each loop, we'll increase the range by 2 times.
        low = high
        high = high * 2
        logging.debug('current index range is %s - %s', low, high)

    # by now, we have got the range in which item to be searched for is present.
    logging.info('selected range is %s - %s', low, high)

    # now that we have range from low to high, we can apply BS here

    # First approach could be little more efficient

    # approach 1
    # find the element such that current element is 1 and previous is 0
    # that would be the first 1 in the given array
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == 1 and arr[mid-1] == 0:
            # This is the first 1 as previous element is 0
            return mid
        elif arr[mid] == 0:
            # We are still in 0s. Move to right array for 1s
            low = mid + 1
        else:
            # We are in 1s now. Move to left for first 1
            high = mid - 1
    return -1


    # approach 2
    # In this approach, whenever we find 1, we store it as this could be
    # potential candidate and keep searching
    # the idea here is,
    # When we find 1:
    #   store the index in result
    #   keep searching in left(smaller elements) array.
    # When we find 0:
    #   Search in right(bigger element) array
    # by now, the main condition would have turned fase as low and high index
    # would have merged. The element in result would be the first 1
    res = -1
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == 1:
            high = mid - 1
            res = mid
        else: #arr[mid] == 0:
            low = mid + 1
    return res

arr = [1, 1, 1, 1, 1]
res = first_one_in_infinity_sorted_binary_array(arr)
print(res)

arr = [0, 0, 0, 0, 0, 0, 0, 0, 1]
res = first_one_in_infinity_sorted_binary_array(arr)
print(res)

arr = [0, 0, 0, 1, 1, 1, 1, 1]
res = first_one_in_infinity_sorted_binary_array(arr)
print(res)

with open("/Users/anbabula/Movies/BinarySearchTechnique/inf_sorted_binary_array.txt", 'r') as inf_bin_array_file:
    #inf_bin_array = inf_bin_array_file.read()
    inf_bin_array = list(map(int, inf_bin_array_file.readlines()))

res = first_one_in_infinity_sorted_binary_array(inf_bin_array)
print(res)
