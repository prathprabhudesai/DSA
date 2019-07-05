''' this is a python implementation of a doubly linked list '''

class DLL_NODE:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, value):
        # this function will push at head
        node = DLL_NODE(value)
        if (self.head):
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = self.tail = node
        self.size += 1

    def pop_head(self):
        if (self.size == 0):
            print("List is empty")
            return
        if (self.size == 1):
            node = self.head
            self.head = self.tail = None
        else:
            node = self.head
            self.head = self.head.next
        self.size -= 1
        return node

    def pop_back(self):
        if (self.size == 0):
            print("List is empty")
            return
        if (self.size == 1):
            node = self.head
            self.head = self.tail = None
        else:
            node = self.tail
            self.tail = self.tail.prev
        self.size -= 1
        return node

    def push_back(self, value):
        # this function will push at tail
        node = DLL_NODE(value)
        if (self.tail):
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = self.tail = node
        self.size += 1

    def delete(self, value):
        # this function deletes a first node with value as input value
        if (self.size == 0):
            print("List is empty")
            return
        if (self.size == 1 and self.head.value == value):
            node = self.head
            self.head = self.tail = None
        else:
            curr = self.head
            i = 0
            while(curr and i < self.size):
                node = curr
                if (curr.value == value):
                    if (curr.next):
                        curr.next.prev = curr.prev
                    if (curr.prev):
                        curr.prev.next = curr.next
                    if curr == self.head:
                        self.head = curr.next
                    if curr == self.tail:
                        self.tail = curr.prev
                    self.size -= 1
                    return node
                else:
                    curr = curr.next
                    i += 1

    def printl(self):
        print("\nList: [ head <-> "),
        curr = self.head
        i = 0
        while(curr and i < self.size):
            print(curr.value),
            print(' <-> '),
            curr = curr.next
            i += 1
        print(" tail ]")

    def printl_rev(self):
        print("\nList: [ rear <-> "),
        curr = self.tail
        i = 0
        while(curr and i <self.size):
            print(curr.value),
            print(' <-> '),
            curr = curr.prev
            i += 1
        print(" head ]")

    def flush(self):
        self.head = self.tail = None
        self.size = 0

if __name__ == "__main__":
    l = DLL()
    l.push_back(4)
    l.push(6)
    l.push(9)
    l.push_back(10)
    l.push_back(20)
    l.push(7)
    l.printl()
    l.printl_rev()
    l.pop_head()
    l.pop_back()
    l.printl()
    l.delete(9)
    l.printl()
    l.delete(10)
    l.printl_rev()
    l.flush()
    l.push(1)
    l.push_back(2)
    l.push(1)
    l.push_back(2)
    l.delete(1)
    l.delete(2)
    l.printl_rev()
