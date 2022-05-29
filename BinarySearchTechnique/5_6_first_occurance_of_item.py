# Following operations in ascending sorted array
# 1. First occurance of an element
# 2. Last occurance of an element
# 3. Count of element x

def first_occurance_of_item(arr, item):
    low = 0
    high = len(arr) -1
    result = -1
    while low <= high:
        mid = low + ((high - low)//2)
        if arr[mid] == item:
            # item found; Don't return yet.
            # Store the index in result and keep searching left
            # for 1st occurance
            result = mid
            high = mid -1
        elif item < arr[mid]:
            high = mid -1
        else:
            low = mid + 1
    return result

def last_occurance_of_item(arr, item):
    low = 0
    high = len(arr) - 1
    result = -1
    while low <= high:
        mid = low + ((high - low)//2)
        if item == arr[mid]:
            # item found; Don't return yet.
            # Store the index in result and keep searching right
            # for 1st occurance
            result = mid
            low = mid + 1
        elif item < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return result

def count_of_elements(arr, n, x):
    first = first_occurance_of_item(arr, x)
    if first == -1:
        return -1
    last = last_occurance_of_item(arr, x)
    if last == -1:
        return -1
    result = last - first + 1
    return result
