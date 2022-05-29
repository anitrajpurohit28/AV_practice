# Minimum window substring
"""
Problem Statement:
    Give a array and a list of required characters, find the minimum sized subarray
    in which all the required characters are present.
Logic:
    Parse the pattern string and store the character and occurance of each character in a
    dictionary as required_dict {char: occurance}
    Values in required_dict means the item is required for value number of times.
    When all the values in required_dict is 0, means no more characters are required. Current
    window contains all the required characters.

    For every window, we might have to check if all the values of the dictionary are 0. It is
    going to be an expensive operation. Check inefficient code below.
    We can avoid this by using a variable called match_count. Match_count to be initilized with
    unique character in given pattern. When a character is fully matched(number of occurance of
    one character), decrement the match_count. When the match_count becomes 0, it means, all the
    string are matched and it is an anagram.
"""
import logging
logging.basicConfig(level=logging.DEBUG)
def min_window_with_all_required_char(arr: list, required_chars:list):
    required_dict = {}

    # First, let us store the required character list in dictionary so that we have list of required
    # characters; We'll call it required_dict

    # required_dict will keep track of the items remaining for current window to have all the required
    # characters
    # Initially, it should be copy of the pattern dictionary
    # example required_dict{a: 2, b: 1} means, 2 a's and 1 b is required for current window to
    # have all the required characters

    for item in required_chars:
        required_dict[item] = required_dict.get(item, 0) +1

    required_count = len(required_dict)
    logging.debug("\n Given Arr: %s\n required_char: %s\n required_dict: %s\n required_count: %s", 
                    arr, required_chars, required_dict, required_count)
    i = 0
    j = 0
    # We shall initilize the min window size and min window as infinity
    min_window_size = float("inf")
    min_window = ""

    # loop to scan all the characters till end of the array
    while j < len(arr):
        logging.debug("arr[j]: %s; required_count: %s; req_dict: %s", arr[j], required_count, required_dict)
        if arr[j] in required_dict.keys():
            # if current character is present in required_dict, it means, we need to consider
            # this character.
            # We found one of the required character and thus,
            # We'll decrement the count of this char from required_dict
            # NOTE required_dict[arr[j]] may get negative if required characters are found in excess
            required_dict[arr[j]] -= 1
            if required_dict[arr[j]] == 0:
                # after decrementing the current character, we shall check if the current character
                # is still more required. If not, we should decrement required_count variable;
                required_count -= 1
            logging.debug("%s is in required list; req_count: %s req_dict: %s",
                            arr[j], required_count, required_dict)
        if required_count != 0:
            logging.debug("Yet to meet the required characters")
        else:
            # Control comming here means, all the required characters are found in the current window
            # Let us note the current window size and current window elements
            current_window_size = j-i+1
            current_window = arr[i:j+1]
            if current_window_size < min_window_size:
                # if current window size is smaller than the min_window_size, overwrite the minimum
                # window size to the current window
                min_window_size = current_window_size
                min_window = current_window
                logging.debug("This is the minimum found so far: Window: %s, size: %s",
                                min_window, min_window_size)
            logging.debug("Found all the required chars; Win: %s; Count: %s",
                            current_window, current_window_size)

            # Now that current window contains all the required characters, lets shring the window
            # and check if it still contains all the required characters.
            logging.debug("Start shrinking from left")
            while required_count == 0:
                logging.debug("Popping %s from current window %s", arr[i], arr[i:j+1])
                # Pre processing before shrinking the window from left
                if arr[i] in required_dict.keys():
                    required_dict[arr[i]] += 1
                    if required_dict[arr[i]] > 0:
                        required_count += 1
                logging.debug("req_count: %s, req_dict: %s", required_count, required_dict)
                # Shrinking the window from the left
                i += 1
                if required_count == 0:
                    # After shrinking the window, the required characters are still found the current window.
                    # Shrink and note the new window size.
                    current_window_size = j-i+1
                    current_window = arr[i:j+1]
                    logging.debug("Current window; Win: %s; Count: %s", current_window, current_window_size)

                if current_window_size < min_window_size:
                # if current window size is smaller than the min_window_size, overwrite the minimum
                # window size to the current window
                    min_window_size = current_window_size
                    min_window = current_window
                    logging.debug("This is the minimum found so far: Window: %s, size: %s",
                                    min_window, min_window_size)
        # Sliding the window to the right;
        j += 1
    logging.info("Minimum window: %s; window_size: %s", min_window, min_window_size)
    return min_window, min_window_size



input_string = "1212453251"
required_string = "123"
window, size = min_window_with_all_required_char(input_string, required_string)
logging.info("Window: %s; Size: %s", window, size)

print("-----")
input_string = "totkkkcootokc"
required_string = "toc"
window, size = min_window_with_all_required_char(input_string, required_string)
logging.info("Window: %s; Size: %s", window, size)


print("-----")
input_string = "time to practice"
required_string = "toc"
window, size = min_window_with_all_required_char(input_string, required_string)
logging.info("Window: %s; Size: %s", window, size)


# Method 2; Inefficient
# Minimum window substring
def is_all_chars_found(passed_dict: dict):
    for k, v in passed_dict.items():
        if v > 0:
            return False
    return True

def min_window_with_all_required_char_inefficient(arr: list, required_chars:list):
    required_dict = {}
    for element in required_chars:
        required_dict[element] = required_dict.get(element, 0) +1
    logging.info("Given string:%s", arr)
    logging.info("Required Dict: %s", required_dict)
    i = 0
    j = 0
    j_increment = True
    min_window_size = float("inf")
    min_window = ""
    while j < len(arr):
        if j_increment:
            logging.debug("current_req_dict: %s; Current window: %s;", required_dict, arr[i:j+1])
            if arr[j] in required_dict.keys():
                required_dict[arr[j]] -= 1
        if not is_all_chars_found(required_dict):
            j+= 1
            j_increment = True
        else:  #  is_all_chars_found(required_dict) == True:
            logging.info("All elements found in window: [%s]; size: %s",
                         arr[i:j+1], len(arr[i:j+1]))
            min_window_size = min(min_window_size, j-i+1)
            min_window = arr[i:j+1]
            logging.debug("min_window: [%s]; min_window_size: %s", min_window, min_window_size)
            # Now, try to shrink the window size
            logging.debug("Now trying to shrink")
            while is_all_chars_found(required_dict):
                min_window_size = min(min_window_size, j-i+1)
                min_window = arr[i:j+1]
                logging.debug("before shrinking, min_size: %s; window: %s", min_window_size, arr[i:j+1])
                logging.debug("popping 1st char '%s' from string: %s;", arr[i], arr[i:j+1])
                if arr[i] in required_dict.keys():
                    required_dict[arr[i]] += 1
                i += 1
                logging.debug("after shrinking, window: %s; required_dict: %s", arr[i:j+1], required_dict)
            j += 1
            j_increment = True
    return min_window, min_window_size
