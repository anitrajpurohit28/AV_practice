# Sort an array using recursion

"""
Problem statement:
    Sort the given array in ascending order, using recursion.
Logic:
    Break the input array
    sort_array: This function will keep reducing the input by popping the last
                item into temp variable say last_item. Once length of array is
                one, start calling insert_item with current array and last_item
                which was popped before calling insert_item.
    sudo code:  if len(array) == 1:
                    return arr
                else:
                    pop last_item from arr
                    sort_array
                    append the last_item popped to array.

    NOTE: array of single number on itself is sorted in ascending and descending
    insert_item: This function takes two args. Array and item to be inserted.
                if the item to be insert is larger than arr[top] just append the
                item otherwise, keep popping the last item to temp variable say,
                last_item till array is empty or the last item is larger than
                item to be inserted. append the popped item to the array.
    sudo code:  if len(array) == 0 OR item >= array[top]:
                    append item to array;
                else item < array[top]:
                    pop the last element to temp variable say last_item, and
                    call insert_item on reduced array.
                    append the last popped last_item to array.
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def insert_item(arr: list, item: int):
    if len(arr) == 0 or arr[-1] <= item:
        arr.append(item)
        logging.debug("insert_item: After appending %s; arr: %s", item, arr)
    else:
        logging.debug("insert_item:item to insert %s < arr[top] %s", item, arr)
        last_item = arr.pop(-1)
        logging.debug("insert_item: after popping %s, arr: %s.", last_item, arr)
        insert_item(arr, item)
        arr.append(last_item)

def sort_array(arr: list):
    if len(arr) == 1:
        return arr[0]
    last_item = arr.pop(-1)
    logging.debug("sort_array: After popping %s; arr: %s", last_item, arr)
    sort_array(arr)
    logging.debug("sort_array: insert %s to arr %s", last_item, arr)
    insert_item(arr, last_item)

    print("sort_array: Sorted array: ", arr)

input_list = [5, 3, 2, 4, 1]
sort_array(input_list)


input_list = [9,8,7,6,5,4,3,2,1]
sort_array(input_list)
