# Nearest Smallest index to the left
# This problem is same as the probem 4_stack_nearest_smallest_to_Left.
# but just the index is to be given
# as answer.

# Program Logic:
# ------------
# 1. Iterate:
# xxx -> Highest/lowest
# Right to Left: if need to find next xxx element to the right
# Left to Right: if need to find next xxx element to the left
#
# Items pushed onto stack will be like (index, element)
# 2. Populate the output array using the core logic
#     Iteams will be pushed as pair onto stack, in format(index, value)
#     For all elements in input array, traversed from left to right
#        a. If stack is empty,
#            append index "-1" to the output_list
#        b. if stack is not empty AND item is smallest than stack[top][item]
#            append stack[top][index] to the output_list
#        c. If stack is not empty AND item is greater than stack[top][item]
#              Do till stack is not empty and stack[top][item] > element:
#                  keep popping the element from stack till stack[top][item] lesser than current item
#              if s[top][item] smaller then the current_item found, insert s[top][index] to the output_list
#              if no such element is found and stack is all popped, append index "-1" to the output_list
#        d. Insert the current (index, element) on top of stack
#
# 3. Insert the current item to the Stack (Irrespective)
#
from my_logger import get_my_logger

def nearest_smallest_index_to_left_inefficient(arr: list):
    logger = get_my_logger(10)
    logger.debug("Input array: %s", arr)
    output_index_list = []    # Will be used to store the resultant indices
    stack = []          # Will be used to keep track of elements on right
    # (index, item) will be pushed on to stack

    # Traverse the aray from left to right is asked in the problem
    for index, item in enumerate(arr):
        # if stack is empty, append index -1; This will be hit for first element
        if len(stack) == 0:
            logger.debug("First iteration; stack is empty. append: %s", item)
            output_index_list.append(-1)
        # if top of stack element is smaller than current item, append s[top] to output
        elif stack[-1][1] < item:
            logger.debug("s[top] is smaller. append to output")
            output_index_list.append(stack[-1][0])
        else: #stack[-1][1] > item:
            # We hit this when s[top] is greater than the current element and stack is not empty
            while len(stack)!= 0 and stack[-1][1] >= item:
                # Keep popping will we find the bigger element on stack
                # OR all the elements on stack are pooped out
                stack.pop(-1)
            if len(stack) == 0:
                # All the elements on stack are popped out
                logger.debug("Stack is all empty after popping; append -1 to output")
                output_index_list.append(-1)
            else:
                # after popping few elements, we found a smaller element on stack
                logger.debug("We found a smaller element on top of stack; "
                              "append index %s to output", stack[-1][0])
                output_index_list.append(stack[-1][0])

        # irrespective of what is popped from stack and what is append to output
        # we need to insert current part(index, item) on top of stack for further processing
        logger.debug("inserting the (%s, %s) onto stack", index, item)
        stack.append((index, item))
        logger.debug("...looping...")

    logger.info("Output index: %s", output_index_list)
    return output_index_list


def nearest_smallest_index_to_left(arr: list):
    stack = []
    op = []
    for index, element in enumerate(arr):
        if not stack:
            op.append(-1)
        else:
            while stack and stack[-1][1] >= element:
                stack.pop()

            if not stack:
                op.append(-1)
            else:
                op.append(stack[-1][0])
        stack.append((index, element))
    return op

input_arr = [6, 2, 5, 4, 5, 1, 6]
res = nearest_smallest_index_to_left(input_arr)
print(res)

