#Generate parentheses
from turtle import back
from my_logger import get_my_logger

def generate_parentheses(n):
    logger = get_my_logger()
    stack = []
    result = []

    def backtracking(openN, closeN):
        logger.debug('OpenN: [%s] closeN: [%s]; stack: %s', openN, closeN, stack)
        if openN == closeN == n:
            logger.debug('appending %s to result', ''.join(stack))
            result.append(''.join(stack))
            return

        if openN < n:
            logger.debug('Adding (')
            stack.append('(')
            backtracking(openN+1, closeN)
            stack.pop()
            logger.debug('Popping ( from top; open: %s; close: %s', openN, closeN)

        if closeN < openN:
            logger.debug('Adding )')
            stack.append(')')
            backtracking(openN, closeN+1)
            stack.pop()
            logger.debug('Popping ) from top; open: %s; close: %s', openN, closeN)

    backtracking(0,0)
    return result

res = generate_parentheses(3)
print(res)