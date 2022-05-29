# Maximum of all subarrays of size K
# arr: Input array
# k: Window size

"""
Problem statement:
    Given an array, and number K, return an array which is consist of max of all
    the subarrays of size K
Solution:
    We can create a sliding window and move the window for each subarray.
    Since we need max of all the subarrays, we can store all the items of each subarray
    in a temperory place. We can have two approach to store the data in temp list
    1. Heap structure. This would be ideal as we can get the max on top of the heap.
    2. List: We need to run the function "max" for each of subarray. It looks natural
        but very inefficient
Logic:
    1. Heap Structure:
        Have i and j point to the two ends of the window;
        while j < len(arr):
            push the item a[j] in heap
            if len(window) < k:
                increase the window size
            else:
                append the top of heap item to output array
                Before moving the window to right, preprocess
                if arr[i] == heap_top:
                    # left most item(arr[i]) is heap's top.
                    pop the top item from the heap.

    2. List Structure:
        Have i and j point to the two ends of the window;
        current_window = []
        while j < len(arr):
            append item(arr[j]) to current_window
            if len(window) < k:
                increase the window size
            else:
                max_item = max(current_window)
                append the max_item to output array
                pop the left most item from current_window
                Move the window to the right
"""
import logging
import heapq
logging.basicConfig(level=logging.DEBUG)

def max_of_all_subarrays_heap_efficient(arr: list, k: int):
    logging.info("Input array: %s", arr)
    i = 0
    j = 0
    output_list = []  # Output result
    max_heap = []  # Temp array to store the subarray items in heap
    while j < len(arr):
        # Push the item to the heap irrespective.
        # Since we need to find the max of all the subarrays,
        # we need to implement the max_heap. Since python
        # have min_heap only, we using min_heap with negation technique to implement
        # the max_heap.
        heapq.heappush(max_heap, arr[j]*-1)
        ##### debug only start #####
        heap_contains = [item*-1 for item in max_heap]
        logging.debug("Current window: %s; Heap contains: %s", arr[i:j+1], heap_contains)
        ##### debug only end #####

        if j-i+1 < k:
            logging.debug("Window size is %s; < %s", j-i+1, k)
            # Do nothing; Just increase the current window size
        else:
            # First item of max_heap is the maximum element, we need to use negation
            # technique as it is max_heap
            heap_top = max_heap[0]*-1
            # Append the top item to the output array
            output_list.append(heap_top)
            logging.debug("current windows: %s; max_item: %s; output_list: %s",
                            arr[i:j+1], heap_top, output_list)
            if arr[i] == heap_top:
                # left most item of the window is the max item; When we move the window,
                # the left item will be lost. We need to pop it from the heap as well.
                logging.debug("Popping %s; heap: %s", heapq.heappop(max_heap)*-1, max_heap)
            # Shrink window from left
            i += 1

        # move the window to the right
        j += 1
    return output_list


def max_of_all_subarrays_max_inefficient(arr: list, k: int):
    logging.info("Input array: %s", arr)
    i = 0
    j = 0
    output_list = []  # Output array
    current_window = []  # Temperory array to store all the elements of current window
    while j < len(arr):
        # append the item to the window irrespective
        current_window.append(arr[j])
        logging.debug("Current window: %s", current_window)
        if j-i+1 < k:
            logging.debug("i: %s; j: %s; Window size(%s) < %s;", i, j, j-i+1, k)
            # Do nothing; Just increase the current window size
        else:
            # Append the max element of current window to output
            output_list.append(max(current_window))
            # Pop the left most element arr[i] from the current window
            temp = current_window.pop(0)
            logging.debug("popped: %s; Current window: %s; output_list: %s",
                            temp, current_window, output_list)
            # Shrink window from left
            i += 1

        # move the window to the right
        j += 1
    return output_list

input_arr = [2, 3, 3, 2, 1, 1, 4, 5, 6, 7, 6, 9]
res = max_of_all_subarrays_heap_efficient(input_arr, 3)
print(res)
print("---------------")
res = max_of_all_subarrays_max_inefficient(input_arr, 3)
print(res)

# input_arr = [1, 3, -1, -3, 5, 3, 6, 7]
# res = max_of_all_subarrays_heap_efficient(input_arr, 3)
# print(res)
