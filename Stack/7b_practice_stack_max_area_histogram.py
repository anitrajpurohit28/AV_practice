from my_logger import get_my_logger

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
        if not stack:
            logger.debug('Stack is empty; appending -1')
            op.append(len(arr))
        else:
            while stack and stack[-1][1] >= element:
                logger.debug('Stack[top]: %s is greater; pop it', stack[-1])
                stack.pop()

            if not stack:
                logger.debug('Stack is empty after popping. append -1')
                op.append(len(arr))
            else:
                logger.debug('Stack[top] %s is smaller; append index %s', stack[-1], stack[-1][0])
                op.append(stack[-1][0])
        logger.debug('Appending %s to stack', (index,element))
        stack.append((index, element))
    return op[::-1]

def max_area_of_histogram_NSR_NSL(a):
    logger = get_my_logger()
    nsr_array = nearest_smallest_index_to_right(a)
    nsl_array = nearest_smallest_index_to_left(a)
    logger.info('Given array: %s', a)
    width_array = []
    for i in range(len(a)):
        width_array.append(nsr_array[i] - nsl_array[i] - 1)

    histogram_area = []
    for i in range(len(a)):
        histogram_area.append(width_array[i]*a[i])
    logger.info('\nNSR: %s;\nNSL: %s;\nWidth_array: %s;\nhistogram_array: %s', nsr_array,
                nsl_array, width_array, histogram_area)
    return max(histogram_area)

a = [6, 2, 5, 4, 5, 1, 6]
res = max_area_of_histogram_NSR_NSL(a)
print('max_area_of_histogram_NSR_NSL:', res)
