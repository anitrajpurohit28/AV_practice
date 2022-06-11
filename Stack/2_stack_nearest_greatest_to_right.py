# Nearest Greatest to right/ Next largest Element to Right

# Identification:
# 1. Input is array/string
# 2. brute force algo:
#     for (i=0;i<n;i++)
#       for(j=i;j<n;j++)
#           if(arr[j] > arr[i]){
#               output[k] = arr[j]
#           }
# Brute force with efficiency O(n2) could be observed;
# Thus it is a stack problem


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
#            append "-1" to the output_list
#        b. if stack is not empty AND item is smaller than stack[top]
#            append stack[top] to the output_list
#        c. If stack is not empty AND item is greater than stack[top]
#              Do till stack is not empty and stack[top] < element:
#                  keep popping the element from stack till stack[top] lesser than current item
#              if s[top] greater then the current_item, insert s[top] to the output_list
#              if no such element is found and stack is all popped, append "-1" to the output_list
#
# 3. Insert the current item to the Stack (Irrespective)
#
# 4. We need to reverse the output array for the final result as we had traversed from right to left.

from my_logger import get_my_logger

# logger = logging.getLogger('stack')
# logger.setLevel(logging.DEBUG)

# console_handler = logging.StreamHandler()
# formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s',
#                                 datefmt='%d-%m-%y %H:%M:%S')
# console_handler.setFormatter(formatter)
# logger.addHandler(console_handler)


def nearest_greatest_to_right_inefficient(arr: list):
    logger = get_my_logger(10)
    logger.debug("Input array: %s", arr)
    output_list = []    # Will be used to store the results
    stack = []          # Will be used to keep track of elements on right

    # Traverse the aray from Right to left as great to right is asked in the problem
    for item in arr[::-1]:
        logger.debug("current item: %s\nOutput: %s\nStack: %s", item, output_list, stack)
        # if stack is empty, append -1; This will be hit for first element
        if len(stack) == 0:
            logger.debug("First iteration; stack is empty. append: %s", item)
            output_list.append(-1)
        # if top of stack element is greater than current item, append s[top] to output
        elif stack[-1] > item:
            logger.debug("s.top (%s) is greater. append %s to output", stack[-1], stack[-1])
            output_list.append(stack[-1])
        else:  #stack[-1] < item:
            # We hit this when s[top] is less than the current element and stack is not empty
            while len(stack) != 0 and stack[-1] < item:
                # Keep popping will we find the bigger element on stack
                # OR all the elements on stack are pooped out
                logger.debug("Popping %s from stack", stack[-1])
                stack.pop(-1)
            if len(stack) == 0:
                # All the elements on stack are popped out
                logger.debug("Stack is all empty after popping; append -1")
                output_list.append(-1)
            else:
                # after popping few elements, we found a bigger element on stack
                logger.debug("We found a bigger element on top of stack; append s.top(%s) to output", stack[-1])
                output_list.append(stack[-1])
        # irrespective of what is popped from stack and what is append to output
        # we need to insert current item on top of stack for further processing
        logger.debug("inserting the current element: [%s] onto stack", item)
        stack.append(item)
        logger.debug("...looping...")

    # since we travelled in reverse order, from Right to left, our result is also
    # reverse. We'll have to reverse to get the correct output
    logger.debug("All processing is done and we have the reversed result")
    output_list = output_list[::-1]
    logger.info("Output is: [%s]", output_list)
    return output_list


def nearest_greatest_to_right(arr: list):
    logger = get_my_logger(10)
    logger.debug("Input array: %s", arr)
    stack = []
    op = []
    for element in arr[::-1]:
        if not stack:
            logger.debug('stack empty append -1')
            op.append(-1)
        else:
            logger.debug('elem: %s; stack: %s; stack[-1]: %s', element, stack, stack[-1])
            while stack and stack[-1] < element:
                popped = stack.pop()
                logger.debug('Popped: %s', popped)
            if not stack:
                logger.debug('stack empty after popping; append -1')
                op.append(-1)
            else:
                logger.debug('stack[top] greater; appending %s', stack[-1])
                op.append(stack[-1])
        logger.debug('default: append %s', element)
        stack.append(element)
        logger.debug('Without reverse stack:%s op: %s', stack, op)
    return op[::-1]


a1 = [1, 3, 2, 4]
res = nearest_greatest_to_right(a1)
print(res)
print("--------")

a2 = [1, 3, 0, 0, 1, 2, 4]
res = nearest_greatest_to_right(a2)
print(res)
print("--------")

a2 = [3, 5, 2, 6, 9, 7, 8]
res = nearest_greatest_to_right(a2)
print(res)
print("--------")

a2 = [9, 8, 6, 7, 4, 5, 2, 3]
res = nearest_greatest_to_right(a2)
print(res)
print("--------")
