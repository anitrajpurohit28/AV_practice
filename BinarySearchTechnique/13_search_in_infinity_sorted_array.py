import logging
logging.basicConfig(level=logging.DEBUG)

def find_in_infinity_sorted_arr(arr, item):
    """
    Find for in element in infinity sorted array.
    Logic:
        For infinity sorted array, we can't apply BS as we don't have
        high index.
        We'll check the range in which item could be found by increasing
        the range by 2 for every cycle.

        Once we find the range, apply regular BS on the range.
    """
    low = 0
    high = 1

    # Try to find th range in which item could be found
    while arr[high] < item:
        # for each loop, we'll increase the range by 2 times.
        low = high
        high = high * 2
        logging.debug('current range is %s - %s', arr[low], arr[high])

    # by now, we have got the range in which item to be searched for is present.
    logging.info('selected range is %s - %s', arr[low], arr[high])

    while low <= high:
        mid = low + (high-low)//2
        logging.debug('Current mid: %s', mid)
        if arr[mid] == item:
            logging.debug('Item found at %s position', mid)
            return arr[mid]
        elif item < arr[mid]:
            high = mid -1
        else:
            low = mid + 1
    logging.debug('Item NOT found')
    return -1

# read a really big list of numbers from a file

# smaller list for testing
# with open(file='inf_arr_small.txt', mode='r') as inf_arr_file:
#     inf_arr_str = inf_arr_file.read()
with open(file='inf_arr_newLine.txt', mode='r') as inf_arr_file:
    inf_arr_str = inf_arr_file.read()

# convert the read numbers into a list
inf_arr = list(map(int, inf_arr_str.split()))

item = 192002
# search for item in the read array
logging.info('item to be found: %s', item)
res = find_in_infinity_sorted_arr(inf_arr, item)
# if res != -1:
#     logging.info('item found at: %s', res)
# else:
#     logging.info('item NOT found')