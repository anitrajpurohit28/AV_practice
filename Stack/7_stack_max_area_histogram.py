# Max Area of Histogram
# Given a list of values which represent the size of histogram,
# find out the maximum area in histogram
# Example:
# input: 6, 2, 5, 4, 5, 1, 6
# output: 6, 10, 5, 12, 5, 7, 1

"""
    Program logic:
    --------------
    Area = Length * breadth(width)
    Length is given array itself
    We need to calculate the width;
    Calculate the width using NSR and NSL algorithm.
    Width of any entry in histogram is NSR - NSL -1;
    # -1 because NSL column itself will be excluded and we need to consider NSL column too
    NSR: Nearest smallest to Right, with smallest right index is len(arr) itself
    NSL: Nearest Smallest to Left, with smallest left index is -1
    input:  6,  2, 5,  4, 5, 1, 6    << Length
    Width:  1,  5, 1,  3, 1, 7, 1
    output: 6, 10, 5, 12, 5, 7, 1  << Length * Width

    return the max from th calculated area

Identification:
    To find the NSR and NSL, we need to use stack as mentioned in previous problems
"""

import logging
logging.basicConfig(level=logging.INFO)

def nearest_smallest_index_to_left(arr: list):
    logging.debug("Input array: %s", arr)
    output_index_list = []    # Will be used to store the resultant indices
    stack = []          # Will be used to keep track of elements on right
    # (index, item) will be pushed on to stack

    # Traverse the aray from left to right is asked in the problem
    for index, item in enumerate(arr):
        # if stack is empty, append index -1; This will be hit for first element
        if len(stack) == 0:
            logging.debug("First iteration; stack is empty. append: %s", item)
            output_index_list.append(-1)
        # if top of stack element is smaller than current item, append s[top] to output
        elif stack[-1][1] < item:
            logging.debug("s[top] is smaller. append to output")
            output_index_list.append(stack[-1][0])
        else: #stack[-1][1] > item:
            # We hit this when s[top] is greater than the current element and stack is not empty
            while len(stack)!= 0 and stack[-1][1] >= item:
                # Keep popping will we find the bigger element on stack
                # OR all the elements on stack are popped out
                # Note: Even if the previous values are equal, we need to keep 
                # popping to check any values are higher
                stack.pop(-1)
            if len(stack) == 0:
                # All the elements on stack are popped out
                logging.debug("Stack is all empty after popping; append -1 to output")
                output_index_list.append(-1)
            else:
                # after popping few elements, we found a smaller element on stack
                logging.debug("We found a smaller element on top of stack; "
                              "append index %s to output", stack[-1][0])
                output_index_list.append(stack[-1][0])

        # irrespective of what is popped from stack and what is append to output
        # we need to insert current part(index, item) on top of stack for further processing
        logging.debug("inserting the (%s, %s) onto stack", index, item)
        stack.append((index, item))
        logging.debug("...looping...")

    logging.info("Output index: %s", output_index_list)
    return output_index_list


def nearest_smallest_index_to_right(arr: list):
    logging.debug("Input array: %s", arr)
    output_index_list = []    # Will be used to store the results
    stack = []          # Will be used to keep track of elements on right\

    # Traverse the aray from Right to left as great to right is asked in the problem
    for index in range(len(arr)-1, -1, -1):
        item = arr[index]

        logging.debug("current item: %s\nOutput: %s\nStack: %s", item, output_index_list, stack)
        # if stack is empty, append -1; This will be hit for first element
        if len(stack) == 0:
            logging.debug("First iteration; stack is empty. append: %s", item)
            output_index_list.append(len(arr))
        # if top of stack element is lesser than current item, append s[top] to output
        elif stack[-1][1] < item:
            logging.debug("s[top][item] %s is lesser. append to output", stack[-1][1])
            output_index_list.append(stack[-1][0])
        else:  #stack[-1][1] > item:
            # We hit this when s[top][item] is greater than the current element and stack is not empty
            while len(stack) != 0 and stack[-1][1] > item:
                # Keep popping till we find the smaller element on stack
                # OR all the elements on stack are popped out
                logging.debug("Popping %s from stack", stack[-1])
                stack.pop(-1)
            if len(stack) == 0:
                # All the elements on stack are popped out
                logging.debug("Stack is all empty after popping; append %s", len(arr))
                output_index_list.append(len(arr))
            else:
                # after popping few elements, we found a smaller element on stack
                logging.debug("We found a smaller element on top of stack; append %s to output", stack[-1][0])
                output_index_list.append(stack[-1][0])
        # irrespective of what is popped from stack and what is append to output
        # we need to insert current item on top of stack for further processing
        logging.debug("inserting the current element: [%s] onto stack", (index, item))
        stack.append((index,item))
        logging.debug("...looping...")

    # since we travelled in reverse order, from Right to left, our result is also
    # reverse. We'll have to reverse to get the correct output
    logging.debug("All processing is done and we have the reversed result")
    output_index_list = output_index_list[::-1]
    logging.info("Output is: [%s]", output_index_list)
    return output_index_list

def max_area_of_histogram_NSR_NSL(arr: list):
    max_NSR = nearest_smallest_index_to_right(arr)
    max_NSL = nearest_smallest_index_to_left(arr)

    logging.info("MAX_NSR: %s", max_NSR)
    logging.info("MAX_NSL: %s", max_NSL)
    arr_width = []
    for i in range(len(arr)):
        # Here we'll consider pseudo index.
        # -1: index smaller then left most building; -1 would mean ground (height = 0)
        # len(a), 0index array+1 : Index higher than the right most building;
        # this would mean ground (height = 0)
        # We'll do '-1' in last because when subtracting left index, we would have subtracted including
        # left building which is not what we want
        # Thus formula would be
        # width of building[i] = right[i] - left[i] -1
        arr_width.append(max_NSR[i] - max_NSL[i] -1)
    logging.info("Max Width of each entry: %s", arr_width)

    # By now, we have the length of each histogram, which is given in argument
    # We have calculated the width of array.
    area_histogram = []
    for index, height in enumerate(arr):
        area_histogram.append(height*arr_width[index])
    logging.info("Area of histogram: %s", area_histogram)
    logging.info("Max area of histogram: %s", max(area_histogram))
    return max(area_histogram)


# input_arr = [6, 2, 5, 4, 5, 1, 6]
# max_area_of_histogram_NSR_NSL(input_arr)




## This method can be used but is rather more complex; dont use

#### Method 2: Stack based, simple algorithm ###
# 1. If the current value is equal or greater then top of stack
#  -> Add the element to stack
# 2. Else, remove the element from top of stack till the stack
#    contains the value smaller or equal to the given value
# 3. Everytime a value is popped, calculate the max area
#
# Idea here is, if the top element of stack is smaller, its index
# will have NSL value and current index is NSR value
def max_area_of_histogram_stack(a: list):
    stack = []
    area = -1
    index = 0

    # This loop will run till all the items are processed
    while index < len(a):
        if len(stack) == 0 or a[index] > stack[-1][0]:
            # if stack is empty or current_item >= stack's top item
            # Just push on top of stack and continue
            stack.append((a[index], index))
            index += 1
            continue
        else:  # a[index] < s[-1][0]
            # stack is not empty and current item is less than
            # item on top of stack
            # We need to pop the items from the stack till stack is
            # either empty or s[top item] < current item
            # The reason we should check the current item with stack[top] is
            # because top of stack will always have smallest index on the left
            while len(stack) != 0:
                if a[index] > stack[-1][0]:
                    # Again, same condition as above, to insert the item
                    # This is when we incur the stack's top element being
                    # smaller than that of current_item
                    stack.append((a[index], index))
                    index += 1
                    break
                else:
                    # The current_item is smaller than the top of stack
                    # Pop the item and calculate the area
                    pop_item = stack.pop()
                    if len(stack) == 0:
                        # This happens when current item is smallest item so far
                        # all the other elements are popped. Thus area is calculated as
                        # popped item * current index
                        width = index - 0  # 0 because this is min element
                    else:
                        # this is when we incur smaller element on the top of the stack
                        # Meaning, Nearest smaller element on the left. We need the calculate
                        # the width as current index - stack's top element +1
                        # index: This points to next item
                        # pop_item[0]: value of item popped from stack

                        # stack[-1][1]: Index of Nearest smallest Left (NSL) element;
                        # +1: because stack[-1][1] would have given NSL and we need to consider
                        #     element after NSL
                        width = index - (stack[-1][1] +1)
                    max_area_from_current_index = pop_item[0] * width
                    area = max(area, max_area_from_current_index)

    # Now, we've incurred end of input array;
    # We may still have elements pushed on stack. we need to calculate it just like above
    while len(stack) != 0:
        pop_item = stack.pop()
        # remember: index still points to the last element
        if len(stack) == 0:
            # width is index of popped item
            width = index # index OR pop_item[1] +1  # +1 because count started from 0
            max_area_from_current_index = pop_item[0] * width
        else:
            # Since all the elements are parsed, and this is the smallest element
            # from the right side(NSR).
            # NSR: index as this is the smallest element from Right
            # NSL: stack[-1][1] Top index of stack
            # +1: because stack[-1][1] would have given NSL and we need to consider
            #     element after NSL
            width = index - (stack[-1][1] + 1)
            max_area_from_current_index = pop_item[0] * width
        area = max(area, max_area_from_current_index)

    return area

a = [6, 2, 5, 4, 5, 1, 6]
res = max_area_of_histogram_NSR_NSL(a)
print('max_area_of_histogram_NSR_NSL:', res)

# a = [2, 1, 2, 3, 1]
# res = max_area_of_histogram_NSR_NSL(a)
# print('max_area_of_histogram_NSR_NSL:', res)

# a = [1, 2, 4, 0, 2, 3, 2]
# res = max_area_of_histogram_NSR_NSL(a)
# print('max_area_of_histogram_NSR_NSL:', res)

# a = [1, 2, 4]
# res = max_area_of_histogram_NSR_NSL(a)
# print('max_area_of_histogram_NSR_NSL:', res)

# a = [1, 2, 3, 4, 5]
# res = max_area_of_histogram_NSR_NSL(a)
# print('max_area_of_histogram_NSR_NSL:', res)

#===============

# a = [6, 2, 5, 4, 5, 1, 6]
# res = max_area_of_histogram_stack(a)
# print('max_area_of_histogram_stack:', res)

# a = [2, 1, 2, 3, 1]
# res = max_area_of_histogram_stack(a)
# print('max_area_of_histogram_stack:', res)

# a = [1, 2, 4, 0, 2, 3, 2]
# res = max_area_of_histogram_stack(a)
# print('max_area_of_histogram_stack:', res)

# a = [1, 2, 4]
# res = max_area_of_histogram_stack(a)
# print('max_area_of_histogram_stack:', res)

# a = [1, 2, 3, 4, 5]
# res = max_area_of_histogram_stack(a)
# print('max_area_of_histogram_stack:', res)