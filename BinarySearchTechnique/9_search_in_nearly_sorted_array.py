# Searching in Nearly(almost) sorted array
import logging

logging.basicConfig(level=logging.DEBUG)
def search_in_nearly_sorted_array(arr, item):
    """
    Binary search on nearly sorted array
    Array is Nearly sorted array when item to be present at ith index
    is present in i/i+1/i-1 index.

    Logic:
        Along with regular comparison of BS, we'll check if item
        is present in mid-1 and mid+1 position;
        before checking for mid-1 and mid+1, have appropriate condition
        to check for IndexError
        If item is not present at mid position, we can move the low/high
        index by 2 as we have already searched for mid+1/mid-1 too
    """
    low = 0
    high = len(arr) -1

    while low <= high:
        mid = low + (high - low)//2
        if item == arr[mid]:
            logging.debug('Item found at index %s', mid)
            return mid
        elif mid - 1 >= 0 and arr[mid-1] == item:
            # check if item is present at mid-1
            logging.debug('Item found at index %s', mid-1)
            return mid - 1
        elif mid + 1 <= len(arr)-1 and arr[mid+1] == item:
            # check if item is present at mid+1
            logging.debug('Item found at index %s', mid+1)
            return mid + 1
        elif item < arr[mid]:
            # move the high by 2 positions as we have already
            # checked for mid-1;
            high = mid - 2
        else:  #item > arr[mid]:
            low = mid + 2
    logging.debug('Item NOT found')
    return -1


print('===============')
arr1 = [5, 15, 10, 20, 40, 30]
result = search_in_nearly_sorted_array(arr1, 30)
print(result)
print('===============')
