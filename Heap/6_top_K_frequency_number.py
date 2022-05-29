# top K frequency number
import logging
# FORMAT = "[%(filename)s:%(lineno)s - %(funcName)s()] %(message)s"
#logging.basicConfig(format=FORMAT, level=logging.info)
logging.basicConfig(level=logging.DEBUG)


####### Approach 1, using built-in methods Counter and sorting #########
from collections import Counter

def top_k_frequency_builtin(arr, top_k):
    frequency_dict = Counter(arr)
    result_list = []
    logging.debug("Frequency array: %s", frequency_dict)

    # Sort based on frequency; frequency is the 2nd item in pair.
    sorted_list = [(k,v) for k, v in sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)]
    for i in range(top_k):
        result_list.append(sorted_list[i])
    return result_list

# input_arr="aaaaabbccccddddddddee"
# res = top_k_frequency_builtin(input_arr, 2)
# logging.info("Resultant list = %s", res)

####### Approach 2, using heap #########

import heapq

def top_k_frequency_numbers(arr, k_value):
    """
        Here we'll store the array variable along with its frequency as a tuple.
        While pushing the element onto heap, we'll push with frequency as the key.
        Since we need to find the element with max frequency, we need to implement the min heap.
        By default, the heap in heapq is min heap.
    """
    heap_k = []
    frequency_dict = {}
    for element in arr:
        frequency_dict[element] = frequency_dict.get(element, 0) +1
    # OR
    # for element in arr:
    #     if element in frequency_dict:
    #         frequency_dict[element] += 1
    #     else:
    #         frequency_dict[element] = 1
    logging.info("Frequency array: %s", frequency_dict)

    for k, v in frequency_dict.items():
        heapq.heappush(heap_k, (v, k))
        if len(heap_k) > k_value:
            logging.info("Popped item: %s", heapq.heappop(heap_k))
    return heap_k

input_arr="aaaaabbccccddddddddee"
k = 3
result = top_k_frequency_numbers(input_arr, k)
logging.info("The top %s frequent elements are: %s", k, result)
