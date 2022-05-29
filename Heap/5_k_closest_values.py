# K closest Numbers
import heapq
import logging
logging.basicConfig(level=logging.DEBUG)

input_arr = [3, 4, 5, 6, 7, 8, 9, 10, 11]
k = 3
x = 7

def k_closest_element(arr, k, x):
    """
        To find the closest values, we should get the absolute difference of all the values
        from the given value. the item with least absolute difference is the closest value.

        To find the closest value, we need to reject/ignore the values whose absolute
        difference is higher but in min-heap, the value with the least difference will be popped.
        Thus we need to use the max heap. Since there is no built-in DS for max, heap,
        we'll use the negation technique.
    """
    heap_k = []
    for element in arr:
    # Push all the items in pairs(abs(element-x, element) onto heap.
    # We mean to use max heap so that maximum values could be popped first.
    # since python library provides min heap only, we'll use negation technique
        heapq.heappush(heap_k, (abs(element-x)*-1, element))
        if len(heap_k) > k:
            # This means, we have pushed more than K elements onto heap where question
            # is to only find K closest elements.
            # Pop from heap. The max difference element will be popped(max_heap)
            popped = heapq.heappop(heap_k)
            logging.debug("Popped value: %s", (popped[0]*-1, popped[1]))

    # Now, the contents of heap are K closest elements only.
    # store it in output list and return
    closest_values = []
    while len(heap_k) > 0:
        # pop each heap elements and store it in output array
        # We are going to swap the stored values from (diff, value) to (value, diff)
        # since we are using max heap, we will use negation technique

        # NOTE: Since we are using max heap, the items will be stored in descending
        # order of the absolute difference. We will have to reverse the array if the
        # values are expected in ascending order
        diff, value = heapq.heappop(heap_k)
        closest_values.append((value, diff*-1))

    ### debug only start ###
    # for value, diff in closest_values:
    #     logging.debug("Value: %s, Diff: %s", value, diff)
    ### debug only end ###

    return closest_values


if __name__ == '__main__':
    # k = int(input("Enter the K value: "))
    # x = int(input("Enter the element for which the closest is to be found: "))
    res = k_closest_element(input_arr, k, x)
    logging.info("%s closest values of %s are: %s", k, x, res)
