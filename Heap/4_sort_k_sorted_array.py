# 4. sort a K sorted array OR K nearly sorted array
# k sorted means the element which was suppose to be at ith index could be found in
# range of i-k or i+k index
import heapq
import logging
logging.basicConfig(level=logging.DEBUG)

def k_sorted_array(arr, k):
    """
    k sorted means the element which was suppose to be at ith index could be found in
    range of i-k or i+k index.
    Logic:
        here logic is, we keep inserting the element into the heap till the count k
        after which we'll keep popping the (front) element and pushing the new element
        Popping the front element makes sure the least element is popped out and the popped
        elements are stored in an sorted array, which is what we are looking for.
    """
    heap_k = []
    sorted_array = []
    for element in arr:
        heapq.heappush(heap_k, element)
        if len(heap_k) > k:
            sorted_array.append(heapq.heappop(heap_k))
    while len(heap_k) > 0:
        sorted_array.append(heapq.heappop(heap_k))
    return sorted_array


if __name__ == '__main__':
    input_arr = [6, 5, 3, 2, 8, 10, 9]
    logging.info("Input array: %s")
    # k = int(input("Enter the K value: "))
    # res = k_sorted_array(input_arr, k)
    k = 3
    res = k_sorted_array(input_arr, k)
    logging.info("%s sorted element: %s", k, res)
