class Stack:

    # constructor
    def __init__(self):
        self.items = []    # item property created

    # empty stack
    def is_empty(self):
        # return len(self.items) == 0
        return not self.items

    # insert item at the top of the stack
    def push(self, item):
        self.items.append(item)

    # extracts top most element and returns it
    # removed from the stack
    def pop(self):
        if not self.items:
            return None
        else:
            return self.items.pop()

    # deletes the "reference" item from stack
    def peek(self):
        return self.items[-1]

    # stack size
    def size(self):
        return len(self.items)

    # inspection
    def __str__(self):
        return str(self.items)


# if this is the main file that's being run,
# then execute the following code
if __name__ == "__main__":
    s = Stack()
    print(s)
    #
    # # enter item
    # s.push(12)
    # s.push(23)
    # print(s)