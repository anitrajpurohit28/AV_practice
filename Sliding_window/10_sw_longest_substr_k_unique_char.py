# Longest substring with K unique characters
import logging
logging.basicConfig(level=logging.DEBUG)

"""
Problem Statement:
    Given an array, we need to find the longest subarray with K unique characters.
    NOTE: Repetations are allowed. Same items could be repeated N times.
Solution:
    Since we need to find K unique characters, irrespective of their occurance, we
    can use dictionary with item as keys(unique) and occurance as values.
    When the len of dictionary is less than k, we have not incurred k unique characters yet
    when len of dict == k unique characters are met; 
        Subarray is from range i to j;
        subarray length = j - i + 1;
    when len of dict > k; more than k unique characters are incurred.
        Keep popping item from dictionary till the len of dict is k;
        

Logic:
    Have i and j point to the two ends of the window;
    while j < len(arr):
        if increment right:
            insert the item in dictionary
        item: no of occurance
        if len(dict) < K:
            need more elements in dictionary
            increment right
        elif len(dict) == k:
            Found the dict with k unique characters.
            length of subarray is j-i+1
            max_subarray = max(max_subarray, j-i+1)
            increment right
        else:
            #Len of dict is more than k
            # remove the leftmost element from dictionary;
            item_dict[arr[i]] -= 1
            # if item count is 0, pop the element from dict
            if item_dict[arr[i]] == 0:
                item_dict.pop(arr[i])
            # This is required to reduce the dictionary size
            # else dict size will not reduce len of dict will
            # only increment and never decrement;
"""

def longest_substring_k_unique_characters(arr: list, k: int):
    logging.debug("Input string: %s", arr)
    i = 0
    j = 0
    longest_substring = 0
    item_dict = {}
    while j < len(arr):
        # Increment the right corner of window
        item_dict[arr[j]] = item_dict.get(arr[j], 0) +1
        logging.debug("Next element: %s; item_dict: %s", arr[j], item_dict)
        if len(item_dict) < k:
            # Length of dict is not yet K; Thus keep parsing for more characters
            logging.debug("The length of dict is not yet %s, continue", k)
        elif len(item_dict) == k:
            # k unique characters are incurred; calculate the size of subarray and
            # store it in longest_subarray if it is more than max longest_subarray;
            logging.debug("Length of dict = %s; Longest_substring so for was: %s; "
                          "current substring: %s", k, longest_substring, arr[i:j+1])
            longest_substring = max(longest_substring, j-i+1)
            logging.debug("New max_unique_len: %s", longest_substring)
        else: # len(item_dict) > k:
            logging.debug("Length of dict[%s] > %s", len(item_dict), k)
            # more than k unique elements are incurred; keep popping till the size of
            # dict is k; Remove from left most position(i)
            while len(item_dict) != k:
                item_dict[arr[i]] = item_dict[arr[i]] -1
                # if count of char dict is 0, remove the entry from the dict; This is
                # important to keep tracking the unique characters and it is equated to
                # length of dictionary itself.
                if item_dict[arr[i]] == 0:
                    item_dict.pop(arr[i])
                logging.debug("Popping %s from dict; item_dict: %s", arr[i], item_dict)
                i += 1
            logging.debug("Dict after popping: %s", item_dict)
        # We need to increment the right corner

        j += 1  # NOTE: The j is out of all the if-else condition; Increment the J irrespective
    logging.debug("Longest substring with %s unique characters is %s", k, longest_substring)
    return longest_substring

input_arr = "ppqerreekelle"
k = 3
res = longest_substring_k_unique_characters(input_arr, k)
logging.info("Longest substring with %s unique characters is %s", k, res)

print("------")

input_arr = "abaccab"
k = 2
res = longest_substring_k_unique_characters(input_arr, k)
logging.info("Longest substring with %s unique characters is %s", k, res)

print("------")

input_arr = ["car", "heli", "animal", "car", "car", "truck", "truck", "heli"]
k = 2
res = longest_substring_k_unique_characters(input_arr, k)
logging.info("Longest substring with %s unique characters is %s", k, res)
