# Build a custom `Stack` similar to the `Queue` you built

# Stack data structure should implement at least four methods
# # PUSH adds an element to the collection
# # POP removes the most recently added element from the collection
# # EMPTY checks whether there are any elements in the stack
# # PEEK returns the topmost element without removing it from the stack


class Stack:
    def __init__(self, data=None):
        self.__stack = []
        if data:
            self.__stack.append(data)

    def push(self, data):
        """adds an element to the collection"""
        self.__stack.append(data)

    def pop(self):
        """removes the most recently added element from the collection"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.__stack.pop()
    
    def is_empty(self):
        """checks whether there are any elements in the stack"""
        return not bool(self.__stack)
    
    def peek(self):
        """returns the topmost element without removing it from the stack"""
        if self.is_empty():
            return None
        return self.__stack[-1]
    
