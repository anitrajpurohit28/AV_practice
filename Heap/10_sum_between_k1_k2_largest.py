# Sum of elements between K1 largest/smallest and K2 smallest

import heapq
import logging
logging.basicConfig(level=logging.DEBUG)

def sum_between_two_largest(arr, k1, k2):
    heap_k1 = []
    heap_k2 = []

    # find the K1 largest element
    for item in arr:
        heapq.heappush(heap_k1, item)
        if len(heap_k1) > k1:
            heapq.heappop(heap_k1)

    k1_largest_element = heapq.heappop(heap_k1)
    logging.debug("K1 %s largest: %s", k1, k1_largest_element)

    # find the K2 largest element
    for item in arr:
        heapq.heappush(heap_k2, item)
        if len(heap_k2) > k2:
            heapq.heappop(heap_k2)

    k2_largest_element = heapq.heappop(heap_k2)
    logging.debug("K2 %s largest: %s", k2, k2_largest_element)

    # Now traverse the array and sum all the elements which are in range
    # K1 and K2, exclude K1 largest and K2 largest
    high_range = max(k1_largest_element, k2_largest_element)
    low_range = min(k1_largest_element, k2_largest_element)
    # OR
    # high_range = k2_largest_element if k2_largest_element > k1_largest_element else k1_largest_element
    # low_range = k2_largest_element if k2_largest_element < k1_largest_element else k1_largest_element
    logging.debug("High range: %s; Low range: %s", high_range, low_range)

    # Traverse the element and consider the element which are in high and low range for addition
    result_sum = 0
    for item in arr:
        if low_range < item < high_range:
            result_sum += item
    logging.debug("Result: %s", result_sum)
    return result_sum

input_arr = [1, 3, 12, 5, 15, 11, 18]
res = sum_between_two_largest(input_arr, 2, 5)
print(res)
