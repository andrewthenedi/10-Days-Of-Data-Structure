class Stack:
    def __init__(self, limit = 1000):
        self.items = []
        self.top_item = None
        self.size = 0
        self.limit = limit
    def is_empty(self):
        return self.size == 0
    def peek(self):
        if not self.is_empty():
            self.top_item = self.items[-1]
            print(self.top_item)
        else:
            print('The stack is empty')
    def get_value(self):
        print(self.top_item)
    def get_stack(self):
        print(self.items)
    def push(self, value):
        self.size = len(self.items)
        if len(self.items) <= self.limit:
            self.size += 1
            self.items.append(value)
            print(self.items)
            self.top_item = self.items[-1]
            # print(self.top_item)
        else:
            print('All out of space!')
    def set_next_node(self):
        length = len(self.items)
        self.items[length-1] = self.top_item
        print(self.items[length[length-1]])
        return
    def pop(self):
        if not self.is_empty():
            item_to_remove = self.items.pop()
            print(item_to_remove)
        else:
            print('The stack is empty')
    def has_space(self):
        self.size = len(self.items)
        if self.limit > self.size:
            print("True")
        else:
            print("False")

# node = Stack()
# node.push('value')
# node.push('new item')
# node.push('temp')
# node.peek()
# node.has_space()
# node.pop()
# node.pop()
# node.pop()