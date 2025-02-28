
# 1) create node class

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({self.value})"

# 2) create LinkedList class

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # 3) create append method

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
 
    # 4) create prepend method

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    # 5) create get node method

    def get_node(self, index):
        if index < 0 or index >= self.length:
            return None
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev_node = self.get_node(index - 1)
            new_node.next = prev_node.next
            prev_node.next = new_node
        self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
        else:
            prev_node = self.get_node(index - 1)
            prev_node.next = prev_node.next.next
        self.length -= 1

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.value))
            node = node.next
        nodes.append("None")
        return "->".join(nodes)

ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)

print(ll)

ll.prepend(5)
print(ll)

node = ll.get_node(1)
print(node.value)

print(node)

ll.insert(2, 15)

print(ll)

ll.remove(2)

print(ll)