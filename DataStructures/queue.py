''' this is an implementation of a queue '''

class QUEUE_NODE:
    def __init__(self, value):
        self.value = value
        self.next = None

class QUEUE:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, value):
        node = QUEUE_NODE(value)
        if (self.size == 0):
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.size = self.size + 1

    def dequeue(self):
        if (self.size == 0):
            print ("Queue is empty")
        else:
            dequeued = self.front
            if (self.size == 1):
                self.front = self.rear = None
            else:
                self.front = self.front.next
            self.size = self.size - 1
            return dequeued
                
    def printq(self):
        if (self.size == 0):
            print("Queue is empty")
        else:
            curr = self.front
            print ("[ Front -> "),
            while(curr):
                print(curr.value),
                curr = curr.next
            print (" <- Rear ]")

if __name__ == "__main__":
    print("Welcome to the Queue Implementation")
    q = QUEUE()
    while(1):
        choice = input("\nSelect: 1.Enqueue 2.Dequeue 3.Display 4.Exit: ")
        if (choice == 1):
            value = input("What do you want to insert? ")
            q.enqueue(value)
            q.printq()
        elif (choice == 2):
            q.dequeue()
            q.printq()
        elif (choice == 3):
            q.printq()
        elif (choice == 4):
            break;
        else:
            print("Wrong option")
            
