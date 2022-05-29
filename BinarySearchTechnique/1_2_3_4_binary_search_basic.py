# array sorted in ascending order;
def binary_search_asc(arr, arr_size, item): 
    low = 0
    high = arr_size -1
    while low <= high:
        mid = low + ((high-low)//2)
        if arr[mid] == item:
            return mid
        if item < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def binary_search_descending(arr, arr_size, item): 
    low = 0
    high = arr_size -1
    while low <= high:
        mid = low + ((high-low)//2)
        if arr[mid] == item:
            return mid
        if item > arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def check_if_arr_is_ascending_descending(arr):
    if arr[0] <= arr[len(arr)-1]:
        return 'ascending'
    else:
        return 'descending'

