class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, *nodes):
        self.last = None
        self.length = 0
        self.head = None

    def append(self, value):
        node = Node(value)
        if (self.last is None):
            self.last = node
            self.head = node
        else:
            node.prev = self.last
            self.last.next = node
            self.last = node
        self.length = self.length + 1

    def delete(self, index):
        if (self.last is None):
            pass
        else:
            if (index < self.length):
                if (index == 0):
                   self.head = self.head.next
                   if (self.head is not None):
                       self.head.prev = None
                   self.length -= 1
                else:
                    if (index == self.length - 1):
                        self.last = self.last.prev
                        if (self.last is not None):
                            self.last.next = None
                        self.length -= 1
                    else:
                        val = self.last
                        for i in range(self.length - index - 1):
                            val = val.prev
                        val.prev.next = val.next
                        val.next.prev = val.prev
                        self.length -= 1
    def search(self, index):
        if (self.head is None):
            pass
        else:
            val = self.last
            for i in range(index):
                val = val.prev
            print(val)

    def __repr__(self):
        val = self.head
        string = ''
        for i in range (self.length):
            if (val.next is None):
                string = f"{string}{val.value}"
            else:
                string = f"{string}{val.value} -> "
                val = val.next
        return string

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.delete(1)
print(ll)