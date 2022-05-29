# Count the occurence of Anagrams

# arr: Input array
# k: Window size
# pattern: the input from which all the anagrams are to be matched.

"""
Problem statement:
    Given an input string and a pattern, return the count of anagram of pattern found in the
    given string.
Logic:
    Parse the pattern string and store the character and occurance of each character in a
    dictionary as required_dict {char: occurance}
    Values in required_dict means the item is required for value number of times to make the anagram.
    When all the values in required_dict is 0, means no more characters are required. Current
    window contains the Anagram.

    For every window, we might have to check if all the values of the dictionary are 0. It is
    going to be an expensive operation. Check inefficient code below.
    We can avoid this by using a variable called required_count. required_count to be initilized with
    unique character in given pattern. When a character is fully matched(number of occurance of
    one character), decrement the required_count. When the required_count becomes 0, it means, all the
    string are matched and it is an anagram.

"""
import logging
logging.basicConfig(level=logging.DEBUG)

def occurance_of_anagram(arr, pattern):
    logging.info("Input string: %s; Pattern: %s", arr, pattern)
    required_dict = {}
    anagram_count = 0
    # First, let us store the pattern in dictionary so that we have count of each character
    # for anagram. We'll call it required_dict

    # required_dict will keep track of the items remaining for
    # for current window to become anagram.
    # Initially, it should be copy of the pattern dictionary
    # example required_dict{a: 2, b:1} means, 2 a's and 1 b is required for current window to
    # become an anagram

    for item in pattern:
        required_dict[item] = required_dict.get(item, 0) +1
    logging.debug("Pattern Dict: %s", required_dict)

    # required_count will keep track of pending characters(Not the count of each character)
    # for current window to become anagram;
    # When current window is anagram of pattern, we'll have to match the entire dictionary.
    # Comparing dictionary is an expensive operation, to avoid that, we are using this
    # required_count technique. When required_count becomes 0, it means no more characters are
    # required for current window to become anagram. In other words, it is a anagram
    # Initial value will be equal to number of characters in the pattern
    required_count = len(required_dict)
    i = 0
    j = 0
    # loop to scan all the characters till end of the array
    while j < len(arr):
        if arr[j] in required_dict.keys():
            # if current character is present in required_dict, it means, we need to consider
            # this character for anagram.
            # We found one of the character which will make the anagram and thus,
            # We'll decrement the count of this char from required_dict
            # NOTE required_dict[arr[j]] may get negative if required characters are found in excess
            required_dict[arr[j]] -= 1

            if required_dict[arr[j]] == 0:
                # after decrementing the current character, we shall check if the current character
                # is still more required for making current window to anagram. If not, we should
                # decrement required_count variable;
                required_count -= 1
        logging.debug("j: %s; arr[%s]: %s; required_dict: %s", j, j, arr[j], required_dict)
        # Current window size is less than the pattern length. This obviously cannot become anagram
        # thus just do nothing and increment the window size.
        if j-i+1 < len(pattern):
            logging.debug("The window size is still less than pattern")
        else:
            # When control comes here, it means, the window size is same as the len of parameter;
            # We will either find the anagram or we won't

            # required_count becoming 0 means, we found all the characters, expected number of times.
            # Current window is pointing to anagram. Increment the anagram count.
            if required_count == 0:
                anagram_count += 1
                logging.debug("found anagram [%s]; anagram_count: %s", arr[i:j+1], anagram_count)

            # We are not finding the anagram in the current window. We need to do that pre-processing
            # for sliding the window from the left side.

            # Now, we'll keep popping the left part of window and move the window to right side.
            # Left most part of window will be removed, thus check if this is part of anagram string.
            # if it is part of anagram string, we should add this character as required character in
            # required_dict
            if arr[i] in required_dict.keys():
                if required_dict[arr[i]] == 0:
                    # if this character was fully matched, we'll need to increase the match count because
                    # This character will be needed to make anagram once again.
                    required_count += 1
                    logging.debug("required_dict[%s] won't be 0 now; required_count: %s", arr[i], required_count)
                required_dict[arr[i]] += 1
            else:
                logging.debug("arr[%s]: %s is not part of pattern array", i, arr[i])
            # Now, all the pre-processing is done to move the window to the right, increment the index
            i += 1
        # Sliding the window to the right;
        j += 1
    logging.info("Anagram count is %s", anagram_count)
    return anagram_count



input_string = "aabaabaa"
input_pattern = "aab"
res = occurance_of_anagram(input_string, input_pattern)
print(res)

print("--------")
input_string = "abccabacbaa"
input_pattern = "aab"
res = occurance_of_anagram(input_string, input_pattern)
print(res)




def occurance_of_anagram_inefficient(string_input, pattern):
    pattern_dict = {}  # to store occurance of each element from input pattern
    temp_dict = {}  # To store the pattern map for current window characters
    anagram_count = 0  # count of anagrams; Final result
    i = 0
    j = 0
    k = len(pattern)
    # Populate the dict with element of input pattern
    for element in pattern:
        pattern_dict[element] = pattern_dict.get(element, 0) +1

    while j < len(string_input):
        logging.debug("Currently populated temp_dict: %s; pattern_dict: %s",
                        temp_dict, pattern_dict)
        temp_dict[string_input[j]] = temp_dict.get(string_input[j], 0) +1
        # OR
        # if string_input[j] in temp_dict:
        #     temp_dict[string_input[j]] += 1
        # else:
        #     temp_dict[string_input[j]] = 1

        if j-i+1 < k:
            j += 1
        else:
            if temp_dict == pattern_dict:
                anagram_count += 1
                logging.debug("Found anagram: in range i[%s]-j[%s]", i, j)

            temp_dict[string_input[i]] -= 1
            if temp_dict[string_input[i]] == 0:
                logging.debug("Popping %s, with count 0 from dictionary", string_input[i])
                temp_dict.pop(string_input[i])
            i += 1
            j += 1
    return anagram_count