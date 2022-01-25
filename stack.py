class Stack(): 
    """Stack class.

   """
    def __init__(self, capacity):
        """Parameters
            ----------
            capacity : int
                maximum capacity of the stack."""
        self.capacity = capacity
        self.data = list()

    def push(self,x):
        if self.isFull():
            raise "Stack is Full"
        else:
            self.data.append(x)

    def pop(self):
        """Returns
        -------
        object
            the last element of the stack"""
        return self.data.pop()

    def isEmpty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def isFull(self):
        if len(self.data) == self.capacity:
            return True
        else:
            return False

    def __repr__(self):
        return '[' + ','.join(map(str, self.data)) + ']'

def check_balance(text):
    """Parameters
        ----------
        text : str
            input text for testing balanced parentheses.

        Returns
        -------
        bool
            returns True if text parantheses are balanced, otherwise False
        """

    stack = Stack(10)
    for ch in text:
        if ch == '(':
            stack.push(ch)
        if ch == ')':
            if stack.isEmpty():
                return False
            else:
                stack.pop()
        else:
            pass #do nothing

    if stack.isEmpty():
        return True
    else:
        return False

if __name__ == '__main__':
    stack = Stack(10)
    for i in range(10):
        stack.push(i)
    print(stack)
    while not stack.isEmpty():
        print(stack.pop())

    print(check_balance('(2+6*4-7))'))
    check_balance()
    
    