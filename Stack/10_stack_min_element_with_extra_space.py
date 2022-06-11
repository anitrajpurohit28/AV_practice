import logging
logging.basicConfig(level=logging.DEBUG)

"""
Have two stack:
Stack: to perform actual stack operations
supporting stack: to store all the minimum elements

stack push:
    push element in stack;
    If the element is < supporting_stack[-1]
        push element in supporting stack
stack pop:
    pop element from stack
    if popped element = supporting_stack[-1]
        pop element from supporting stack
stack min:
    return top element of supporting stack
"""
class stack_impl:
    def __init__(self):
        self.s = []  # stack
        self.ss = []  # supporting stack

    def stack_push(self, item):  # redefined the above function for alternative approach
        self.s.append(item)
        if not self.ss or self.ss[-1]>=item:
            self.ss.append(item)

    def _stack_push_inefficient(self, item):
        # Push the element to the stack; We need to do this irrespective
        self.s.append(item)
        # check if element is smaller than supporting_stack[top], if so,
        # copy the element to top of supporting_stack
        if len(self.ss)== 0:
            # We'll hit this code for very first element of array;
            # Just push whatever element found first
            self.ss.append(item)
        # Even if the elements are equal, push onto supporting stack; This
        # is important to handle the duplicate elements
        elif len(self.ss)!= 0 and item <= self.ss[-1]:
            # if the element is smaller, push on to supporting stack as well
            self.ss.append(item)
        logging.debug("item: %s; s: %s; ss: %s", item, self.s, self.ss)

    def stack_pop(self):
        # sanity check on main stack. If the main stack is empty,
        # supporting stack MUST be empty too. Just return
        if not self.s:
            logging.debug("Empty list")
            return
        # we'll need to pop from main stack irrespective
        popped = self.s.pop()

        # if the popped element is on top of supporting stack, pop it from
        # supporting stack too.
        if popped == self.ss[-1]:
            self.ss.pop(-1)
            logging.debug("Popped %s from supporting stack", popped)
        logging.debug("Popped %s from stack", popped)
        logging.debug("s: %s; ss: %s", self.s, self.ss)
        return popped

    def stack_min(self):
        # top of the supporting stack will always have the minimum element
        logging.debug("s: %s; ss: %s", self.s, self.ss)
        if not self.ss:
            logging.debug("Stack empty")
            return
        return self.ss[-1]

    def stack_display(self):
        logging.debug("s: %s; ss: %s", self.s, self.ss)

if __name__ == '__main__':
    stack = stack_impl()
    option = int(input("Enter option:\n1. push\t2. pop\t3. min\t4. display\t 5. Exit\n"))
    while option <=5:
        if option == 1:
            item = int(input("Enter item: "))
            stack.stack_push(item)
        elif option == 2:
            item = stack.stack_pop()
            logging.info("Popped item: %s", item)
        elif option == 3:
            item = stack.stack_min()
            logging.info("Min element: %s", item)
        elif option ==4:
            stack.stack_display()
        else:
            break
        option = int(input("Enter option:\n1. push\t2. pop\t3. min\t4. display\t 5. Exit\n"))
