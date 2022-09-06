# Search for an item in bitonic array:
# Bitonic array is one where element are monotonously increasing
# and then will reach the peak after which it'll monotonously decrease.
# No duplicates can be found in bitonic array
# Only one peak would be found in bitonic array


import logging
logging.basicConfig(level=logging.DEBUG)

def binary_search(a: list, item: int, asc_des_order: str):
    """
    Binary search on given array
    Args:
        a: list of items
        item: Item to be searched for
        asc_des_order: "asc" if array is in ascending order
                       "des" if in descending order
    """
    logging.debug('%s Array: %s', binary_search.__name__, a)
    logging.debug('Order: %s', "Ascending" if asc_des_order == 'asc' else "Descending")
    low = 0
    high = len(a) -1

    while low <= high:
        mid = low + (high-low)//2
        if asc_des_order == 'asc':
            if a[mid] == item:
                logging.debug('%s Item found at %s position', binary_search.__name__, mid)
                return mid
            elif a[mid] < item:
                low = mid + 1
            else:
                high = mid -1
        else:
            if a[mid] == item:
                logging.debug('%s Item found at %s position', binary_search.__name__, mid)
                return mid
            elif a[mid] < item:
                high = mid -1
            else:
                low = mid + 1
    logging.debug('%s Item not found', binary_search.__name__)
    return -1


def search_in_bitonic_array(arr, item):
    """
    Search for an item in bitonic array

    Logic:
    1. Find the peak elements to divide the array in two smaller arrays
    2. Divide the array in two parts, such that
        array1 = 0 to peak-1
        array2 = peak to N
    3. Array1 is ascending sorted; Array2 is descending sorted
    4. Search for element in array1. if element is found, return index
    5. search for element in array2. If element is found, return mid+index
    6. If element is not found found in either, return -1
    """
    logging.debug('Input: %s\nItem: %s', arr, item)
    low = 0
    high = len(arr) -1

    # Divide the array into two arrays such that
    # array1: Elements sorted in ascending order
    # array2: Elements sorted in descending order
    while low <= high:
        mid = low + (high-low)//2
        # Condition for non-edge elements
        if mid > 0 and mid < (len(arr)-1):
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                # we'll divide the array in two from this mid
                arr1 = arr[:mid] # 0 to mid-1
                arr2 = arr[mid:] # mid to end
                logging.debug('divided the array into two '
                              '%s; %s', arr1, arr2)
                break
            elif arr[mid] < arr[mid+1]:
                low = mid+1
            else:
                high = mid -1
        else:
            # We come here only for edge elements
            # This is the last time we are looping, if
            # peak is not found here,
            #       it cannot be a bitonic array
            # if Peak is found,
            #       This is either ascending or descending
            #       sorted array; Don't need to divide in 2
            logging.debug('Edge condition')
            if mid == 0 and arr[mid] > arr[mid+1]:
                # this is an descending sorted array
                arr1 = []
                arr2 = arr[:]
                break
                # OR
                #return binary_search(arr2, item, "des")
            elif mid == len(arr)-1 and arr[mid] > arr[mid-1]:
                # This is ascending sorted array
                arr1 = arr[:]
                arr2 = []
                break
                # OR
                #return binary_search(arr1, item, "asc")
            else:
                logging.error('This is NOT a bitonic array')
                # This is NOT a bitonic array
                return -1

    # if low > high means, no peak element found in given array
    # this shouldn't happen in bitonic array;
    if low > high:
        logging.info('Given array does not look like bitonic array')
        return -1

    # The array is divided into two parts;
    # array1: ascending sorted
    # array2: descending sorted;
    # we need to find the requested item in these two arrays using BS.

    # Search for the item in array1
    res = binary_search(arr1, item, 'asc')
    if res != -1:
        # item is found in array1. return the position
        logging.info('Item found at %s position', res)
        return res
    else:
        # Element is not found in first array;
        # now try searching for item in array2
        res = binary_search(arr2, item, 'des')

    if res != -1:
        # Item is found in 2nd array, return the position
        # position = mid + index returned from BS on array2 as this
        # array would come after mid position
        logging.info('Item found at %s position', mid+res)
        return mid+res
    else:
        # item is not found in either of array;
        logging.info('Item not found')
        return -1

arr = [1, 3, 5, 7, 9, 12, 11, 8, 4]
print(search_in_bitonic_array(arr, 4))
print(search_in_bitonic_array(arr, 1))
print(search_in_bitonic_array(arr, 12))
print(search_in_bitonic_array(arr, 13))
print(search_in_bitonic_array(arr, 2))
print('-----')
arr1 = [1, 3, 5, 7, 9, 12]
print(search_in_bitonic_array(arr1, 4))
print(search_in_bitonic_array(arr1, 1))
