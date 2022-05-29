# Connect the ropes to minimise the cost
"""
Problem statement:
    Given a list of ropes of different length, we need to connect the rope
    such that the cost of connecting is minimum
    Cost of rope is calculated in this fasion
    cost_rope_connection = rope_len_1 + rope_len_2

Solution:
    Push all the rope in min heap
    pop two ropes (2 minimum length rope)
    Join them and calculate the cost of joining them
    Push the resultant rope back to heap
    Repeate these steps till we have only one rope
"""
import heapq
import logging
logging.basicConfig(level=logging.DEBUG)
rope_len = [1, 2, 3, 4, 5]

def min_cost_rope_connect(arr):
    min_heap = []
    # push all the elements onto the heap
    for item in arr:
        heapq.heappush(min_heap, item)

    # now least elements will be popped first.
    # pop two elements, sum them up and push it again
    total_cost = 0
    while len(min_heap) > 1:
        logging.debug("Heap: %s; length: %s", min_heap, len(min_heap))
        first = heapq.heappop(min_heap)
        second = heapq.heappop(min_heap)
        current_cost = first + second
        # get the sum of first two minimum elements
        total_cost = total_cost + current_cost
        logging.debug("First: %s; Second: %s: current_cost: %s Total: %s",
                                first, second, current_cost, total_cost)

        # push the minimum elements back to min_heap
        heapq.heappush(min_heap, current_cost)
    return total_cost

rope_len = [1, 2, 3, 4, 5]
result = min_cost_rope_connect(rope_len)
logging.info(result)

rope_len = [3,6,9,15]
result = min_cost_rope_connect(rope_len)
logging.info(result)
