# Longest substring without repeating characters
# Longest substring with K unique character; K = number of given unique character
"""
Problem statement:
    Find the longest substring such that no element in that substring should be repeated
Logic:
    We can use dictionary for this; When len of dictionary is same as the window size,
    all the characters in window are unique; In such case, find the length and store it.
    If the lenght of dictionary is less than window size, it means we have some duplicate
    items in the dictionary. 
    Keep popping from the left of array, from the dictionary till the length of dictionary
    is same is the window size.
Algo:
    Have i and j point to the two ends of the window;
    for j < len(arr):
        add item in dict

        if len(dict) == window size:
            max_length = max(cur_len, max_len)
        else:
            while len(dic) != window_size:
                Decrement OR pop arr[i] from dict
        j += 1

"""
import logging
logging.basicConfig(level=logging.DEBUG)

def longest_non_repeating_characters(arr: list):
    logging.info("Input arr: %s", arr)
    max_non_repeating_len = 0
    i = 0
    j = 0
    char_dict = {}
    while j < len(arr):
        logging.debug("inserting %s; curr_window: %s", arr[j], arr[i:j+1])
        # insert the element on Right of the window to dictionary,
        # if item is already present, increment count
        char_dict[arr[j]] = char_dict.get(arr[j], 0) + 1
        if len(char_dict) == j-i+1:
            # All the characters incurred in this subarray are unique
            logging.debug("Dict length: %s == window_size: %s; cur_window: %s",
                            len(char_dict), j-i+1, arr[i:j+1])
            max_non_repeating_len = max(max_non_repeating_len, j-i+1)
            logging.info("curr_window_size: %s, max window_size: %s", j-i+1, max_non_repeating_len)
        else: # len(char_dict) < j-i+1:
            # Repeated items are incurred; Keep popping from left of subarray in this block
            logging.debug("Dict length: %s < window_size: %s; cur_window: %s",
                                len(char_dict), j-i+1, arr[i:j+1])
            logging.info("We have repeating chars")
            while len(char_dict) != j-i+1:
                # Keep popping the element till only unique characters are found in dict.
                logging.debug("popping %s", arr[i])
                char_dict[arr[i]] = char_dict[arr[i]] - 1
                if char_dict[arr[i]] == 0:
                    # element with 0 occurance shall we removed from dict so that len(dict)
                    # gives the proper size
                    logging.debug("Removing %s entry from dictionary", arr[i])
                    char_dict.pop(arr[i])
                i += 1
        # Increament the right part of the subarray
        j += 1
        # we'll never have condition where len(char_dict) > j-i+1;
    logging.debug("Max unique length substring is %s", max_non_repeating_len)
    return max_non_repeating_len

input_arr = "pwwkew"
res = longest_non_repeating_characters(input_arr)
logging.info("Max unique char substring is :%s", res)

print("-------")

input_arr = "abcacbabcdeeb"
res = longest_non_repeating_characters(input_arr)
logging.info("Max unique char substring is :%s", res)
