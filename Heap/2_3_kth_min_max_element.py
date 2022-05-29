import heapq
import logging

logging.basicConfig(level=logging.DEBUG)


##### Approach 1, using sorting; nlog(n) ############
# sort the array and return the value a the appropriate index.

# input_arr = [3,4,6,1,2,5,9,8,7]
# print("Input array: %s", input_arr)
# input_arr.sort()
# print(input_arr)
# k = int(input("Enter the kth element: "))
# logging.info("%s smallest: %s",k, input_arr[k-1])
# logging.info("%s largest: %s",k, input_arr[len(input_arr)-k])
# print(input_arr[3])

##### Approach 2, using heap; nlog(k) ############
#Find the "Kth" max and min element of an array


def kth_largest(arr, k):
    # in min heap, elements are always popped from the front(minimum side)
    # thus the array will be remained with the larger elements
    # Kth largest element is always found at base(left) of min heap
    heap_k = []
    for item in arr:
        heapq.heappush(heap_k, item)
        if len(heap_k) > k:
            heapq.heappop(heap_k)
    logging.debug("%s", heap_k)
    return heap_k

def kth_smallest(arr, k):
    # Kth largest element is found at right of max heap
    # since python does not have max heap data structure,
    # we are inserting the negated values, thus highest element will
    # be found at the base(left) part of the array
    #
    # other explaination
    #
    # Since python uses min-heap, the largest element will be on end(back)
    # since the elements are always deleted from the front end, we need to 
    # invert the values such that the elements are to be deleted from back.
    # to achieve this, we negate all the values to be inserted and thus make
    # sure that the highter values are deleted first since higher the values
    # more negative it gets
    heap_k = []
    for item in arr:
        heapq.heappush(heap_k, item*-1)
        if len(heap_k) > k:
            heapq.heappop(heap_k)
    actual_heap_values = [value*-1 for value in heap_k]
    logging.debug("Actual array: %s", actual_heap_values)
    return actual_heap_values

if __name__ == '__main__':
    input_arr = [3,4,6,1,2,5,9,8,7]
    logging.info("Input arr: %s", input_arr)
    k = int(input("Enter the K value: "))
    res = kth_largest(input_arr, k)
    logging.info("%s largest element: %s", k, res)

    res = kth_smallest(input_arr, k)
    logging.info("%s smallest element: %s", k, res)
