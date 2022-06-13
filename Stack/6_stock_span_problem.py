# Given array contains price of particular stock on each day, we need to find the number of days
# the stock price have been smaller or equal BEFORE it.
# Example:
# Input array: [100, 80, 60, 70, 60, 75, 85]
# output:      [  1,  1,  1,  2,  1,  4,  6]

# If we observe carefully enough, this problem is similar to Nearest Greatest element to Left problem

# Identification:
# 1. Input is array/string
# 2. brute force algo:
#     for (i=0;i<n;i++)
#       for(j=i;j>0;j++)
#           if(arr[j] > arr[i]){
#               count ++;
#           }
# Brute force with efficiency O(n2) could be observed;
# observed that the jth loop dependent on ith loop
# Thus it is a stack problem

# Direction of iterate:
# xxx -> Highest/lowest
# Right to Left: if need to find next xxx element to the right
# Left to Right: if need to find next xxx element to the left


from my_logger import get_my_logger

# This is similar to Nearest Greatest element's index to Left problem
def stock_span_problem(arr: list):
    stack = []  # (index, item)
    op = []

    for index, item in enumerate(arr):
        while stack and stack[-1][1] <= item:
            stack.pop()

        if not stack:
            # this can happend when current element is greatest in the stack and thus
            # all the elements are popped out of stack. So, current index is to be pushed
            # Mind +1 as the indices are 0 based numbered.
            # When stack is all empty, there is no element greater to left. We can append "0"
            # but we need to consider current element too. Thus counting the current element,
            # the output should be 1
            op.append(index+1)
        else:
            # No need to add +1 here as all the elements pushed in stack are also 0 based numbers.
            op.append(index - stack[-1][0])
        stack.append((index,item))
    return op


def stock_span_problem_inefficient(arr: list):
    """
        If we observe carefully enough, this problem is similar to Nearest Greatest element to Left problem
    """
    logger = get_my_logger(50)
    stack = []
    output_list = []

    # Since we need all the elements smaller to left(before it), we will traverse from left to right
    for index, item in enumerate(arr):
        if len(stack) == 0:
            # +1 because this will hit only for the 1st element only. we need to count the
            # current day if earlier day is not possible
            logger.debug("1st element; appending %s", index+1)
            output_list.append(index+1)
        elif item < stack[-1][1]:
            # If the current element is lesser than previous element meaning the previous day
            # stock price were greater than today, we'll consider current day only and append 1
            logger.debug("Found element %s larger than current element %s on stack", stack[-1], item)
            output_list.append(1)
        else:
            # We come here if the previous day values are LESS THAN OR EQUAL to todays stock price
            # Keep popping the elements from the stack till we find the value larger than the current
            # price
            while len(stack) != 0 and stack[-1][1] <= item:  # till item greater or equal, pop
                logger.debug("stack top %s is smaller to current item %s, pop", stack[-1], item)
                stack.pop(-1)
            if len(stack) == 0:
                # all the elements of stack are popped. current index is the highest so far;
                # insert current index +1 to stack; +1 because it is 0 indexed array
                # Current index because, no item to left is greater.
                logger.debug("Stack is all empty. Append current index+1: %s, to output", index+1)
                output_list.append(index+1)  # current index + 1 because we need to consider current index too and
                                             # it is 0 based index
            else:
                # We found an element, on stack which is greater than current element
                # current index would be more as previous elements are pushed onto stack
                # to get the distance, we need to subtract current index with stack's top
                # index
                logger.debug("Stack's top %s is larger; append %s - %s", stack[-1], index, stack[-1][0])
                output_list.append(index - stack[-1][0])

        # Push the current index & value onto stack irrespective;
        logger.debug("inserting the current element [%s] onto stack", item)
        stack.append((index, item))
        logger.debug("...looping...")
    logger.info("Output is: %s", output_list)
    return output_list




# a1 = [100, 80, 60, 70, 60, 75, 85]
# print(a1)
# res = stock_span_problem(a1)
# print(res)
# print("---")

# a2 = [74, 665, 742, 512, 254, 469, 748, 445]
# print(a2)
# res = stock_span_problem(a2)
# print(res)
# print("---")

a2 = [74, 665, 742, 512, 254, 469, 748, 445, 663, 758, 38, 60, 724, 142, 330, 779, 317, 636, 591, 243, 289, 507, 241, 143, 65, 249, 247, 606, 691, 330, 371, 151, 607, 702, 394, 349, 430, 624, 85, 755, 357, 641, 167, 177, 332, 709, 145, 440, 627, 124, 738, 739, 119, 483, 530, 542, 34, 716, 640, 59, 305, 331, 378, 707, 474, 787, 222, 746, 525, 673, 671, 230, 378, 374, 298, 513, 787, 491, 362, 237, 756, 768, 456, 375, 32, 53, 151, 351, 142, 125, 367, 231, 708, 592, 408, 138, 258, 288, 554, 784, 546, 110, 210, 159, 222, 189, 23, 147, 307, 231, 414, 369, 101, 592, 363, 56, 611, 760, 425, 538, 749, 84, 396, 42, 403, 351, 692, 437, 575, 621, 597, 22, 149, 800]
# print(a2)
# print("---")
res = stock_span_problem(a2)
print(res)
print("---")


a3 = [74, 665, 742, 512, 254, 469, 748, 445, 663, 758, 38, 60, 724, 142, 330, 779, 317, 636, 591, 243, 289, 507, 241, 143, 65, 249, 247, 606, 691, 330, 371, 151, 607, 702, 394, 349, 430, 624, 85, 755, 357, 641, 167, 177, 332, 709, 145, 440, 627, 124, 738, 739, 119, 483, 530, 542, 34, 716, 640, 59, 305, 331, 378, 707, 474, 787, 222, 746, 525, 673, 671, 230, 378, 374, 298, 513, 787, 491]
res = stock_span_problem(a3)
print(res)
