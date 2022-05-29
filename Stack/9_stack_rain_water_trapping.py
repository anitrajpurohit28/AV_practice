import logging
logging.basicConfig(level=logging.DEBUG)

"""
Logic:
    Water at any block would be minimum of maximum water collectable
    on left side and on right side minus the size of building itself
    water at arr[index] = min(max_left, max_right) - height of building

"""
def populate_max_left(arr: list):
    """
    maximum value of index from left.
    initilize the all the values of max_left list to 0
    iterate from left to right. If current value is greater than max
        max = current value
    store the max value at current index.
    """
    max_left = [0] * len(arr)
    maximum = 0
    for index, item in enumerate(arr):
        if item > maximum:
            # if current item is greater then current max, reassign max
            maximum = item
        max_left[index] = maximum
    return max_left

def populate_max_right(arr: list):
    """
    Maximum value of index from Right.
    Initilize all the values of max_rigth list to 0
    Iterate from right to left. If current value id greater than max
        max = current value
    store the max value at current
    """
    max_right = [0]*len(arr)
    maximum = 0
    for index, item in reversed(list(enumerate(arr))):
        if item > maximum:
            # if current item is greater then current max, reassign max
            maximum = item
        max_right[index] = maximum
    return max_right


def water_trapping(arr: list):
    """
    Water at current index is min(max_left, max_right) - block height
    """
    max_left_array = populate_max_left(arr)
    max_right_array = populate_max_right(arr)
    logging.info("Max Left arr: %s", max_left_array)
    logging.info("Max Right arr: %s", max_right_array)

    water_at_index = [0]*len(arr)

    for index in range(len(arr)):
        water_at_index[index] = min(max_left_array[index], max_right_array[index]) - arr[index]
        logging.debug("Water at index %s: %s; so far: %s", index, water_at_index[index], water_at_index)
    logging.debug(water_at_index)
    return water_at_index

input_arr = [1, 4, 2, 5, 3, 6, 5, 3, 1, 5, 3, 4]
res = water_trapping(input_arr)
print(res)
