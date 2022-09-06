import logging
logging.basicConfig(level=logging.DEBUG)

def next_alphabet_element(arr, item):
    """
    Find the next alphabet in given sorted array
    Even if you find an matching item, always return the next item
    if the given item is not present in array, return possible next item

    Logic:
        Have a temperory variable
        if item is found,
            if index+1 is present,
                return item at index+1
            else:
                return invalid
        if item less than arr[mid]:
            store in result as this is a possible candidate
            continue the search in left subarray
        else if item is greater:
            continue the search in right array
    """
    low = 0
    high = len(arr)-1
    result = '#'
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == item:
            # given item is present, return the next item
            # check if the mid+1 is within the array range
            # if not, return NOT_VALID value
            if mid+1 <= len(arr)-1:
                logging.debug("found the exact item and index+1 is valid")
                return arr[mid+1]
            else:
                logging.debug("found the exact item but index+1 is NOT valid")
                return '#'
        elif arr[mid] > item:
            # the arr[mid] is greater than item, this could
            # be a potential candidate; store it in result
            result = arr[mid]
            logging.debug("current item is greater; %s is potential candidate", result)
            high = mid -1
        else:
            low = mid + 1
    return result


input_arr = ['a', 'b', 'c', 'f', 'h']
res = next_alphabet_element(input_arr, 'f')
print(res)

input_arr = ['a', 'b', 'c', 'f', 'h']
res = next_alphabet_element(input_arr, 'a')
print(res)


input_arr = ['a', 'b', 'c', 'f', 'h']
res = next_alphabet_element(input_arr, 'h')
print(res)

input_arr = ['a', 'b', 'c', 'f', 'h']
res = next_alphabet_element(input_arr, 'd')
print(res)

input_arr = ['a']
res = next_alphabet_element(input_arr, 'd')
print(res)
