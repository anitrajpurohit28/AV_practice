import heapq
import logging
logging.basicConfig(level=logging.DEBUG)

def frequency_sort(arr):
    """
        same as 6th question; Here, keep pushing the elements on heap and once all the
        elements are pushed, keep popping all the elements in the min sorted order.
        Since the request is the sort the elements in descending order, we need to implement
        the max heap.
    """
    heap_k = []
    frequency_dict = {}
    result_arr = []
    # for element in arr:
    #     if element in frequency_dict:
    #         frequency_dict[element] += 1
    #     else:
    #         frequency_dict[element] = 1
    #   #OR
    for element in arr:
        frequency_dict[element] = frequency_dict.get(element, 0) +1

    logging.debug("Frequency dictionary: %s; length: %s", frequency_dict, len(frequency_dict))

    for key, value in frequency_dict.items():
        heapq.heappush(heap_k, (value*-1, key))
    logging.debug("Heap elements: %s; length: %s", heap_k, len(heap_k))

    # implementation of max heap and reverting the order, element followed by frequency
    for i in range(len(heap_k)):
        popped_element = heapq.heappop(heap_k)
        result_arr.append((popped_element[1], popped_element[0]*-1))
    # OR
    """
    while len(heap_k) > 0:
    # pop each heap elements and store it in output array
    # We are going to swap the stored values from (diff, value) to (value, diff)
    # since we are using max heap, we will use negation technique

    # NOTE: Since we are using max heap, the items will be stored in descending
    # order of the absolute difference. We will have to reverse the array if the
    # values are expected in ascending order
    diff, value = heapq.heappop(heap_k)
    closest_values.append((value, diff*-1))
    """
    print(result_arr)

input_arr_numbers = [1,2,2,2,2,3,3,4,4,4,4,4,4,6,6,6,6,6,6,6,6]
input_arr_char = "aabbbbbbbcccccccccccdd"
frequency_sort(input_arr_numbers)
frequency_sort(input_arr_char)
