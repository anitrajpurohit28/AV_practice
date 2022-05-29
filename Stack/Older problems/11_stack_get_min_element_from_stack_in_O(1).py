import logging
logging.basicConfig(level=logging.DEBUG)

class stack:
    def __init__(self):
        self.s = []
        self.min_element = None

    def push(self, x):
        # if stack is empty, just insert the element and update the min_element value
        if len(self.s) == 0:
            self.s.append(x)
            self.min_element = x

        # if element to push is greater than min_element, just push the value;
        # No need to update the minimum element
        elif x > self.getMin():
            self.s.append(x)

        # if item to push is lesser than min_element; Update the min_element
        else:  # x < self.min_element:
            # We won't push the actual value to stack but rather calculated value
            # as per below formula
            stack_push_element = 2*x - self.min_element
            # min_element is update to the newly inserted value
            self.min_element = x
            self.s.append(stack_push_element)
        logging.debug("Append: %s; stack: %s; min_ele: %s", x, self.s, self.min_element)


    def pop(self):
        if len(self.s) == 0:
            logging.debug("Stack empty")
            return -1
        else:
            # Since pop is called, node MUST be popped.
            node_removed_from_stack = self.s.pop()

            # After popping, if stack is empty, update min_element
            if len(self.s) == 0:
                self.min_element = -1

            # check if popped node is greater than min_element, don't update min_element
            if node_removed_from_stack >= self.min_element:
                logging.debug("Popped: %s; stack: %s; min_ele: %s", node_removed_from_stack, self.s, self.min_element)
                return node_removed_from_stack
            else:  # self.s[-1] < self.min_element
                # we need to return min_element as this should have been the top
                # most value to be popped
                to_return = self.min_element
                # need to update the min_element as per following formula
                self.min_element = (2 * self.min_element) - node_removed_from_stack
                logging.debug("Popped: %s; stack: %s; min_ele: %s", node_removed_from_stack, self.s, self.min_element)
                return to_return

    def getMin(self):
        return self.min_element if self.min_element else -1

    def getTop(self):
        if len(self.s) == 0:
            return
        if self.s[-1] >= self.min_element:
            return self.s[-1]
        else:  # self.s[-1] < self.min_element
            return self.min_element

    def print(self):
        print('Stack: ', end=' ')
        for i in range(len(self.s)):
            print(self.s[i], end=' ')
        print()
        print('Min Element:', self.getMin())



s = stack()
option = True
while option:
    option = int(input('1. push\t2. pop\t3. getMin\t4. getTop\t5. print\n'))
    if option == 1:
        element = int(input('Item to push: '))
        s.push(element)
    elif option == 2:
        print(s.pop())
    elif option == 3:
        print(s.getMin())
    elif option == 4:
        print(s.getTop())
    elif option == 5:
        print(s.print())
    else:
        break



#
# if __name__ == '__main__':
#     arr = [2, 1, 16, 3, 2, 2, 1, 50, 2, 3, 2, 3, 2, 3, 2, 1, 27, 2, 2, 3, 3, 1, 30, 3, 3, 3, 2, 2, 2, 3, 1, 23, 1, 70, 1, 94, 2, 2, 2, 1, 74]
#     stk = stack()
#     qi = 0
#     qn = 1
#     while qn < 33:
#         qt = arr[qi]
#         if qt == 1:
#             stk.push(arr[qi+1])
#             qi += 2
#         elif qt == 2:
#             print(stk.pop(), end=' ')
#             qi += 1
#         else:
#             print(stk.getMin(), end=' ')
#             qi += 1
#         qn += 1
#     print()
