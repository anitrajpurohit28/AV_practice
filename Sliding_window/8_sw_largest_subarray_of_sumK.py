# Largest subarray of sum K
import logging
logging.basicConfig(level=logging.DEBUG)
"""
Problem statement:
    Given an array and sum, we need to find all the subarray
    whose sum is equals to given sum. Among those subarraies,
    choose subarray with the maximum length

Logic:
        Have i and j point to the two ends of the window;
        while j < len(arr)
            current sum += arr[j]
            if the current sum == given sum,
                not the window size.
                If current window size is greater,
                    store it as largest window size
                increase window size
            else if current sum < given sum,
                increase window size
            else if current sum > given sum,
                We need to decrease the window size
                subtract the value of left corner before
                moving the left corner
                increase the left corner, i += 1
                dont move window to right

"""
# With one more temp variable to control the expanding and shrinking of window
def largest_subarray_sumk(arr, given_sum):
    logging.debug("Given array: %s", arr)
    i = 0
    j = 0
    curr_sum = 0
    largest_subarray = 0
    while j < len(arr):
        # Increment the right corner of window
        curr_sum = curr_sum + arr[j]
        logging.debug("Curr_sum: %s; array_size[%s-%s]", curr_sum, i,j)
        if curr_sum == given_sum:
            # now that current sum is equal to given sum, Store the
            # len of this sub array if > len of max len subarray stored.
            curr_list_length = j - i + 1
            logging.info("current_sum: %s; current_length: %s, "
                         "largest_subarray: %s; arr_size[%s-%s]",
                           given_sum, curr_list_length, largest_subarray, i, j)
            largest_subarray  = max(curr_list_length, largest_subarray)
            logging.debug("Incrementing jth index")
            # We need to increment the right corner
        elif curr_sum < given_sum:
            # We need to increment the right corner as current sum is still
            # less than the sum we are looking for
            logging.debug("Incrementing jth index")
        elif curr_sum > given_sum:
            # now current sum is greater then the sum we are looking for, we
            # need to shrink the subarray from the left side;
            # remove the left most element from current sum and shrink the left
            # subarray
            logging.debug("curr_sum: %s > given_sum: %s; remove: %s", curr_sum, given_sum, arr[i])
            curr_sum -= arr[i]
            logging.debug("curr_sum: %s; i:%s; j:%s",curr_sum, i, j)
            i += 1
            #when the window size is shrunk, we don't expect the subarray to be larger;
        j += 1  # NOTE the j is out of all the loops;
    return largest_subarray

# # With one more temp variable to control the expanding and shrinking of window
# def largest_subarray_sumk_temp_variable(arr, given_sum):
#     logging.debug("Given array: %s", arr)
#     i = 0
#     j = 0
#     curr_sum = 0
#     largest_subarray = 0
#     j_incremented = True # temp variable to decide if we need to move the window to right or not.
#     while j < len(arr):
#         if j_incremented:
#             # Increment the right corner of window
#             curr_sum = curr_sum + arr[j]
#         logging.debug("Curr_sum: %s; array_size[%s-%s]", curr_sum, i,j)
#         if curr_sum == given_sum:
#             # now that current sum is equal to given sum, Store the
#             # len of this sub array if > len of max len subarray stored.
#             curr_list_length = j - i + 1
#             logging.info("current_sum: %s; current_length: %s, "
#                          "largest_subarray: %s; arr_size[%s-%s]",
#                            given_sum, curr_list_length, largest_subarray, i, j)
#             largest_subarray  = max(curr_list_length, largest_subarray)
#             logging.debug("Incrementing jth index")
#             # We need to increment the right corner
#             j += 1
#             j_incremented = True
#         elif curr_sum < given_sum:
#             # We need to increment the right corner as current sum is still
#             # less than the sum we are looking for
#             logging.debug("Incrementing jth index")
#             j+= 1
#             j_incremented = True
#         elif curr_sum > given_sum:
#             # now current sum is greater then the sum we are looking for, we
#             # need to shrink the subarray from the left side;
#             # remove the left most element from current sum and shrink the left
#             # subarray
#             logging.debug("curr_sum: %s > given_sum: %s; remove: %s", curr_sum, given_sum, arr[i])
#             curr_sum -= arr[i]
#             logging.debug("curr_sum: %s; i:%s; j:%s",curr_sum, i, j)
#             i += 1
#             # Do no increment the right corner
#             j_incremented = False
#     return largest_subarray

input_arr = [4, 1, 1, 1, 2, 3, 5, 8]
max_sum = 5
res = largest_subarray_sumk(input_arr, max_sum)
print(res)
