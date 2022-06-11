# Nearest Smallest to Left/ Next lowest Element to Left

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
#     For all elements in input array, traversed from left to right
#        a. If stack is empty,
#            append "-1" to the output_list
#        b. if stack is not empty AND item is smallest than stack[top]
#            append stack[top] to the output_list
#        c. If stack is not empty AND item is greater than stack[top]
#              Do till stack is not empty and stack[top] > element:
#                  keep popping the element from stack till stack[top] lesser than current item
#              if s[item] smaller then the current_item found, insert s[top] to the output_list
#              if no such element is found and stack is all popped, append "-1" to the output_list
#        d. Insert the current element on top of stack
#
# 3. Insert the current item to the Stack (Irrespective)
#
from my_logger import get_my_logger

def nearest_smallest_to_left_inefficient(arr: list):
    logger = get_my_logger(50)
    logger.debug("Input array: %s", arr)
    output_list = []    # Will be used to store the results
    stack = []          # Will be used to keep track of elements on right

    # Traverse the aray from left to right is asked in the problem
    for item in arr:
        logger.debug("current item: %s\nOutput: %s\nStack: %s", item, output_list, stack)
        # if stack is empty, append -1; This will be hit for first element
        if len(stack) == 0:
            logger.debug("First iteration; stack is empty. append: %s", item)
            output_list.append(-1)
        # if top of stack element is smaller than current item, append s[top] to output
        elif stack[-1] < item:
            logger.debug("s[top] is smaller. append to output")
            output_list.append(stack[-1])
        else:  #stack[-1] > item:
            # We hit this when s[top] is greater than the current element and stack is not empty
            while len(stack) != 0 and stack[-1] >= item:
                # Keep popping will we find the bigger element on stack
                # OR all the elements on stack are pooped out
                logger.debug("item %s > s[top] %s; Popping %s from stack", item, stack[-1], stack[-1])
                stack.pop(-1)
            if len(stack) == 0:
                # All the elements on stack are popped out
                logger.debug("Stack is all empty after popping; append -1 to output")
                output_list.append(-1)
            else:
                # after popping few elements, we found a smaller element on stack
                logger.debug("We found a smaller element on top of stack; append %s to output", stack[-1])
                output_list.append(stack[-1])
        # irrespective of what is popped from stack and what is append to output
        # we need to insert current item on top of stack for further processing
        logger.debug("inserting the current element [%s] onto stack", item)
        stack.append(item)
        logger.debug("...looping...")


    logger.info("Output is: [%s]", output_list)
    return output_list

def nearest_smallest_to_left(arr: list):
    stack = []
    op = []
    for element in arr:
        if not stack:
            op.append(-1)
        else:
            while stack and stack[-1] >= element:
                stack.pop()
            if not stack:
                op.append(-1)
            else:
                op.append(stack[-1])
        stack.append(element)
    return op


a1 = [1, 3, 2, 4]
res = nearest_smallest_to_left(a1)
print(res)
print("--------")

a2 = [1, 3, 0, 0, 1, 2, 4]
res = nearest_smallest_to_left(a2)
print(res)
print("--------")

a2 = [3, 5, 2, 6, 9, 7, 8]
res = nearest_smallest_to_left(a2)
print(res)
print("--------")

a2 = [9, 8, 6, 7, 4, 5, 2, 3]
res = nearest_smallest_to_left(a2)
print(res)
print("--------")
