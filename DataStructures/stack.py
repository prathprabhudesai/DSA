''' this is an implementation of stack using linked list '''

class STACK_NODE:
    def __init__(self, value):
        self.value = value
        self.next = None

        
class STACK:
    def __init__(self):
        self.top = None
        self.size = 0
        
    def push(self, value):
        node = STACK_NODE(value)
        node.next = self.top
        self.top = node
        self.size = self.size + 1

    def pop(self):
        if (self.size == 0):
            print ("Stack is empty")
        else:
            popped = self.top
            self.top = self.top.next
            self.size = self.size - 1
            return popped

    def prints(self):
        if (self.size == 0):
            print ("Stack is empty")
        else:
            print ("[ top -> "),
            curr = self.top
            while (curr):
                print (curr.value),
                curr = curr.next
            print (" ]")

    
if __name__ == "__main__":
    s = STACK()
    s.push(10)
    s.prints()
    s.push(20)
    s.prints()
    s.push(30)
    s.prints()
    s.prints()
    s.pop()
    s.prints()
    s.pop()
    s.prints()
    s.pop()
    s.prints()
    s.pop()
