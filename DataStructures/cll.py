''' this is a python implementation of a circular linked list '''

class CLL_NODE:
    def __init__(self, value):
        self.value = value
        self.next = None

class CLL:
    def __init__(self):
        self.tail = None

    def insert(self, value):
        node = CLL_NODE(value)
        if (self.tail):
            head = self.tail.next
            self.tail.next = node
            node.next = head
            self.tail = node
        else:
            self.tail = node
            node.next = self.tail

    def sorted_insert(self, value):
        if (self.tail):
            node = CLL_NODE(value)
            curr = self.tail.next
            while(curr and curr.next):
                if curr.next.value <= value and curr != self.tail:
                    curr = curr.next
                else:
                    break
            temp = curr.next
            curr.next = node
            node.next = temp
            if (curr == self.tail):
                self.tail = node
        else:
            self.insert(value)

    def printl(self):
        print("\nCircular LL: [ "),
        if (self.tail):
            curr = self.tail.next
            while(curr):
                print(curr.value),
                curr = curr.next
                if (curr == self.tail.next):
                    break
        print(" ]")

    def delete(self, value):
        if (self.tail is None):
            print("List is empty")
            return
        curr = self.tail.next
        if (curr == self.tail):
            self.flush()
        else:
            while(curr and curr.next):
                if (curr.next.value != value and curr != self.tail):
                    curr = curr.next
                else:
                    break
            if (curr.next.value == value):
                node = curr.next
                curr.next = node.next
                if (node == self.tail):
                    self.tail = curr

    def flush(self):
        self.tail = None

    def exchange_first_and_last(self):
        self.tail.value, self.tail.next.value = self.tail.next.value, self.tail.value

        
def get_josephus_position(m, n):
    # m is the skipping interval for the nodes
    # n is the total no of nodes
    # first create a Circular linked list of n nodes
    l = CLL()
    for i in range(n):
        l.insert(i+1)
    l.printl()
    curr = l.tail.next
    for i in range(n-1):
        mcount = 1
        while(mcount <= m-1):
            curr = curr.next
            mcount += 1
        temp = curr
        l.delete(curr.value)
        curr = temp.next
        l.printl()
    l.printl()

        
if __name__ == "__main__":
    '''
    l = CLL()
    l.insert(10)
    l.insert(20)
    l.insert(30)
    l.insert(40)
    l.insert(50)
    l.sorted_insert(25)
    l.sorted_insert(45)
    l.sorted_insert(45)
    l.sorted_insert(55)
    l.insert(70)
    l.delete(25)
    l.delete(70)
    l.printl()
    l.insert(2)
    l.printl()
    l.delete(2)
    l.printl()
    '''
    get_josephus_position(2, 14)
