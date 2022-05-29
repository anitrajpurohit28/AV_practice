import logging

logging.basicConfig(level=logging.INFO)

def floor_of_element_in_sorted_array(arr, item):
    """
    Find the floor of given item in a sorted array
    floor of element = Biggest element smaller then given item in given array

    Logic:
        All the elements lesser than given item are potential candidates
        Proceed with basic BS.
        if item < arr[mid]:
            store it in temp variable called result
            move low to mid + 1
        else:
            high = mid -1
        return the temp "result"
    """
    logging.info('Array: %s\nitem: %s', arr, item)
    low = 0
    high = len(arr) -1
    result = -1
    while low <= high:
        mid = low + (high-low)//2
        # if we find the exact item, return
        if item == arr[mid]:
            logging.debug('Found the exact match')
            return arr[mid]
        if item < arr[mid]:
            # since we are looking for floor, and current element is
            # bigger than given item, this is not a potential candidate
            high = mid - 1
        else:  # item > arr[mid]
            # since the floor is element smaller than given item; 
            # this is a potential condidate.
            logging.debug('Found a potential candidate; %s', arr[mid])
            result = arr[mid]
            low = mid + 1
    
    return result


def ceil_of_element_in_sorted_array(arr, item):
    logging.info('Array: %s\nitem: %s', arr, item)
    low = 0
    high = len(arr) -1
    result = -1
    while low <= high:
        mid = low + (high-low)//2
        if item == arr[mid]:
            logging.debug('Found the exact match')
            return arr[mid]
        if item < arr[mid]:
            # Since we are looking for ceil and current item is larger than
            # the given item, this could serve as potential candidate
            logging.debug('Found a potential candidate; %s', arr[mid])
            result = arr[mid]
            high = mid - 1
        else: # item > arr[mid]
            # since we are looking for ceil and current item is smaller than
            # the given item, this could NOT serve as potential candidate
            low = mid + 1
    return result




logging.info('===============')
arr1 = [23, 34, 56, 77, 88, 99]
result = floor_of_element_in_sorted_array(arr1, 34)
logging.info('Floor: %s', result)
result = ceil_of_element_in_sorted_array(arr1, 34)
logging.info('Ceil: %s', result)
logging.info('===============')

arr1 = [23, 34, 56, 77, 88, 99]
result = floor_of_element_in_sorted_array(arr1, 35)
logging.info('Floor: %s', result)
result = ceil_of_element_in_sorted_array(arr1, 35)
logging.info('Ceil: %s', result)

logging.info('===============')
arr1 = [23, 34, 56, 77, 88, 99]
result = floor_of_element_in_sorted_array(arr1, 100)
logging.info('Floor: %s', result)
result = ceil_of_element_in_sorted_array(arr1, 100)
logging.info('Ceil: %s', result)
logging.info('===============')

