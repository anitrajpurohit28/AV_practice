# K closest points to Origin
# Given pair of indicies (X, Y) axis, find the K pairs which are closest to the origin
# in the 4 quadrants
import heapq
import logging
logging.basicConfig(level=logging.INFO)

input_arr = [(1, 3),
             (-2,2),
             (5, 8),
             (0, 1)]
def k_closest_to_origin(arr, k):
    """
        The distance between a node and origin in 4 quadrant is the line drawn from origin
        to that node, which is longest side on the Right-angle triange. Thus we can
        calculate the distance by using pythagoras theorem a² + b² = c² where c² is the 
        distance of node from origin.
        Store the distance from origin and the item(x, y) itself in a pair
        (distance_from_origin, (x, y)) and push onto the heap. in Min-heap,
        minimum values will be popped out which is NOT what we need. We need to
        pop out the maximum values and store the minimum(nearest) values
    """
    heap_k = []
    for x, y in arr:
        # Calculating the distance² using pythogrous theorem, C² = a² + b²
        distance = abs(x)**2 + abs(y)**2
        # We need to find the closest element thus discard the furtherest element.
        # to discard furtherest elemtent, we will have to use max-heap. Python library
        # doesn't have implementation for max-heap thus will using min-heap with negation technique
        # We'll push element on heap in format (distance, (x, y)). We'll store the distance as 1ˢᵗ
        # arguement so that heap sort will store max element on top, so max distant elements will be
        # popped out(discarded) first.
        logging.debug("Item to insert: (%s, %s); distance: %s", x, y, distance)
        heapq.heappush(heap_k, (distance*-1, (x,y)))
        if len(heap_k) > k:
            # Heap contains more than required elements, popping out the furtherest element which
            # is top of max-heap.
            logging.debug("Popping %s", heap_k)
            heapq.heappop(heap_k)
        logging.debug("Heap contents: %s", heap_k)

    result = []
    while heap_k:
        # We need to store only the item for result and not the distance.
        # Since it is a max heap, the largest/furtherest element will be popped first
        distance, item = heapq.heappop(heap_k)
        result.append(item)

    # since we had used max-heap, elements will be stored from furtherest to closest sorted order.
    # We'll reverse the list to make it closest element first
    result.reverse()
    logging.info("Returning the result: %s", result)
    return result

res = k_closest_to_origin(input_arr, 2)
logging.info("Result: %s", res)

##########
def k_closest_to_origin_long_inefficient_approach(arr, k):
    """
        The distance between a node and origin in 4 quadrant is the line drawn from origin
        to that node, which is longest side on the Right-angle triange. Thus we can
        calculate the distance by using pythagoras theorem A2 + B2 = C2; where c2 is the 
        distance of node from origin.
        Store the distance from origin and the item itself in a pair
        (distance_from_origin, item) and push onto the heap. in Min-heap,
        minimum values will be popped out which is NOT what we need. We need to
        pop out the maximum values and store the minimum(nearest) values
    """
    distance_item_pair_arr = []
    heap_k = []
    for item in arr:
        distance_item_pair_arr.append([((abs(item[0]) ** 2) + (abs(item[1]) ** 2)), item])
    logging.debug("Array populated: %s", distance_item_pair_arr)

    # Since we need to implement the max heap, we'll use the negation technique on min heap
    for i in range(len(distance_item_pair_arr)):
        distance_item_pair_arr[i][0] = distance_item_pair_arr[i][0]*-1
    logging.debug("negated populated: %s", distance_item_pair_arr)

    # push all the items on the array
    for item in distance_item_pair_arr:
        heapq.heappush(heap_k, item)
        if len(heap_k) > k:
            heapq.heappop(heap_k)
    logging.debug("Heap items: %s", heap_k)

    # revert the negation and put the item first followed by distance
    # [(x, y), dist]
    result_arr = []
    for i in range(len(heap_k)):
        heap_k[i][0] = heap_k[i][0]*-1
        result_arr.append((heap_k[i][1], heap_k[i][0]))

    logging.debug("Result_array: %s", result_arr)

    return result_arr
