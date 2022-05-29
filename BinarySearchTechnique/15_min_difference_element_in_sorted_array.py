import logging
logging.basicConfig(level=logging.INFO)

def minimum_difference_element(arr, item):
    """
    Find the minimum difference of a given element and the given array
    Here we need to subtract each item of given array from the item
    and find which one would result in least number.

    Note 1: If the item is present in array, return the item since
        item - item would result in 0, which is minimum
    Note 2: It the item is not present, the items neighbouring to position
        of element would be potential candiates
    Note 3: After applying BS, low and high would have swapped their
        positions and arr[low] got higher number than arr[high]

    Logic:
    1. Apply BS; If item is present, return item
    2. if item is not present low and high would have swapped but those
       are potential results as those would be the items neighbours;
    3. Find the absolute difference of neighbours and return the least one
    """
    logging.info('%s; item=%s', arr, item)
    low = 0
    high = len(arr) - 1

    # 1. applying Binary Search
    while low <= high:
        logging.debug('Array: %s', arr[low:high+1])
        mid = low + (high-low)//2
        logging.debug('mid: %s; arr[mid]: %s', mid, arr[mid])
        if arr[mid] == item:
            logging.info('Found the exact element %s', arr[mid])
            return arr[mid]
        elif arr[mid] < item:
            low = mid + 1
        else:
            high = mid - 1

    # # APPROACH 1
    # as high and low are the neighour of item, those are potential candidates
    # Find the absolute difference with arr[low] and arr[high] and return the appropriate value
    logging.info('Item not found; Potential candidates arr[low]: %s; arr[high]: %s', arr[low], arr[high])
    if abs(item-arr[low]) < abs(item-arr[high]):
        return arr[low]
    else:
        return arr[high]

    # # APPROACH 2
    # Observation is, "mid" would point to next position of where it item to be found is present
    # Thus if the element were present, it would be sandwitched with mid(low) and mid-1(high)
    # after the loop ends, high and low would have swapped thus
    # low = mid
    # high = mid - 1

    # logging.info('Item not found; Current arr[mid]: %s arr[mid-1]: %s', arr[mid], arr[mid-1])
    # logging.debug('Potential candidates are %s and %s', arr[mid-1], arr[mid])
    # if abs(item - arr[mid-1]) < abs(item - arr[mid]):
    #     logging.debug('returning %s', arr[mid-1])
    #     return arr[mid-1]
    # else:
    #     logging.debug('returning %s', arr[mid])
    #     return arr[mid]



arr1 = [1, 4, 6, 8, 10, 13, 16, 19]
res = minimum_difference_element(arr1, 12)
print(res)

res = minimum_difference_element(arr1, 3)
print(res)

res = minimum_difference_element(arr1, 2)
print(res)
