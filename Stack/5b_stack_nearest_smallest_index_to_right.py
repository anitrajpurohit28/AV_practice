# Nearest Smallest index to right/ Next smallest Element index to Right

# Program Logic:
# ------------
# 1. Iterate:
# xxx -> Highest/lowest
# Right to Left: if need to find next xxx element to the right
# Left to Right: if need to find next xxx element to the left
#
# 2. Populate the output array using the core logic
#     For all elements in input array, traversed from right to left
#        a. If stack is empty,
#            append index "len(arr)" to the output_index_list
#        b. if stack is not empty AND item is smaller than stack[top][item]
#            append stack[top][index] to the output_index_list
#        c. If stack is not empty AND item is greater than stack[top][item]
#              Do till stack is not empty and stack[top][item] < element:
#                  keep popping the element from stack till stack[top][item] lesser than current item
#              if s[top][item] smaller then the current_item found, insert s[top][index] to the output_index_list
#              if no such element is found and stack is all popped, append index "len(arr)" to the output_index_list
#        d. Insert the current (index, element) on top of stack(irrespective)
#
# 4. We need to reverse the output array for the final result as we had traversed from right to left.

from my_logger import get_my_logger

def nearest_smallest_index_to_right_inefficient(arr: list):
    logger = get_my_logger(50)
    logger.debug("Input array: %s", arr)
    output_index_list = []    # Will be used to store the results
    stack = []          # Will be used to keep track of elements on right\

    # Traverse the aray from Right to left as great to right is asked in the problem
    for index in range(len(arr)-1, -1, -1):
        item = arr[index]

        logger.debug("current item: %s; Output: %s; Stack: %s", item, output_index_list, stack)
        # if stack is empty, append -1; This will be hit for first element
        if len(stack) == 0:
            logger.debug("First iteration; stack is empty. append index: -1")
            output_index_list.append(-1)
        # if top of stack element is lesser than current item, append s[top] to output
        elif stack[-1][1] < item:
            logger.debug("s[top][item] %s is lesser. append index %s to output", stack[-1][1], stack[-1][0])
            output_index_list.append(stack[-1][0])
        else:  #stack[-1][1] > item:
            # We hit this when s[top][item] is greater than the current element and stack is not empty
            while len(stack) != 0 and stack[-1][1] >= item:
                # Keep popping till we find the smaller element on stack
                # OR all the elements on stack are popped out
                logger.debug("Popping %s from stack", stack[-1])
                stack.pop(-1)
            if len(stack) == 0:
                # All the elements on stack are popped out
                logger.debug("Stack is all empty after popping; append -1")
                output_index_list.append(-1)
            else:
                # after popping few elements, we found a smaller element on stack
                logger.debug("We found a smaller element on top of stack; append index %s to output", stack[-1][0])
                output_index_list.append(stack[-1][0])
        # irrespective of what is popped from stack and what is append to output
        # we need to insert current item on top of stack for further processing
        logger.debug("inserting the current element: [%s] onto stack", (index, item))
        stack.append((index,item))
        logger.debug("...looping...")

    # since we travelled in reverse order, from Right to left, our result is also
    # reverse. We'll have to reverse to get the correct output
    logger.debug("All processing is done and we have the reversed result")
    output_index_list = output_index_list[::-1]
    logger.info("Output is: [%s]", output_index_list)
    return output_index_list

def nearest_smallest_index_to_right(arr: list):
    logger = get_my_logger(50)
    stack = []
    op = []

    # because enumerate function does not count reverse
    # for index in range(len(arr)-1, -1, -1):
    #     element = arr[index]

    # Since we are reversing after enumeration, it'll start from last index only
    for index, element in reversed(list(enumerate(arr))):
        logger.debug('index: %s; element: %s; stack: %s', index, element, stack)
        while stack and stack[-1][1] >= element:
            logger.debug('Stack[top]: %s is greater; pop it', stack[-1])
            stack.pop()
        if not stack:
            logger.debug('Stack is empty after popping. append -1')
            op.append(-1)
        else:
            logger.debug('Stack[top] %s is smaller; append index %s', stack[-1], stack[-1][0])
            op.append(stack[-1][0])
        logger.debug('Appending %s to stack', (index,element))
        stack.append((index, element))
    return op[::-1]

a1 = [1, 3, 2, 4]
res = nearest_smallest_index_to_right(a1)
print(res)
print("--------")

a2 = [1, 3, 0, 0, 1, 2, 4]
res = nearest_smallest_index_to_right(a2)
print(res)
print("--------")

a2 = [3, 5, 2, 6, 9, 7, 8]
res = nearest_smallest_index_to_right(a2)
print(res)
print("--------")

a2 = [9, 8, 6, 7, 4, 5, 2, 3]
res = nearest_smallest_index_to_right(a2)
print(res)
print("--------")

a2 = [6, 2, 5, 4, 5, 1, 6]
res = nearest_smallest_index_to_right(a2)
print(res)
print("--------")
