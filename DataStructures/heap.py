''' this is the python implementaion of min heap '''

INITIAL_SIZE = 1024

class HEAP:
    def __init__(self):
        self.h = [None]*INITIAL_SIZE
        self.size = 0

    @staticmethod
    def left_child_index(i):
        return ((2*i) + 1)

    @staticmethod
    def right_child_index(i):
        return ((2*i) + 2)

    @staticmethod
    def parent_index(i):
        return (int((i-1)/2))

    def has_left_child(self, i):
        return (True if (HEAP.left_child_index(i) < self.size) else False)

    def has_right_child(self, i):
        return (True if (HEAP.right_child_index(i) < self.size) else False)

    def has_parent(self, i):
        return (True if (HEAP.parent_index(i) >= 0) else False)

    def left_child(self, i):
        return self.h[HEAP.left_child_index(i)]

    def right_child(self, i):
        return self.h[HEAP.right_child_index(i)]

    def parent(self, i):
        return self.h[HEAP.parent_index(i)]

    def swap(self, i, j):
        print("called swap")
        temp = self.h[i]
        self.h[i] = self.h[j]
        self.h[j] = temp
    
    def heapify_up(self):
        index = self.size - 1
        while(self.has_parent(index) and (self.parent(index) > self.h[index])):
            self.swap(index, HEAP.parent_index(index))
            index = HEAP.parent_index(index)
        
    def heapify_down(self):
        index = 0
        while(self.has_left_child(index)):
            smaller_child_index = HEAP.left_child_index(index)
            if ((self.has_right_child(index)) and
                (self.right_child(index) < self.left_child(index))):
                smaller_child_index = HEAP.right_child_index(index)
            if self.h[index] < self.h[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)
            index = smaller_child_index
            
    def add(self, value):
        if (self.size > INITIAL_SIZE):
            print("Heap is full.")
            return
        self.h[self.size] = value
        self.size = self.size + 1
        self.heapify_up()
        self.printh()

    def peek(self):
        if self.size == 0:
            return None
        return self.h[0]
        
    def poll(self):
        if self.size == 0:
            print("Heap is empty")
            return None
        value = self.h[0]
        self.h[0] = self.h[self.size - 1]
        self.size = self.size - 1
        self.heapify_down()
        return value

    def printh(self):
        print("\nHeap: "),
        for i in range(self.size):
            print(self.h[i]),
        print("\n")


if __name__ == "__main__":
    h = HEAP()
    h.add(5)
    h.add(7)
    h.add(3)
    h.add(4)
    h.add(2)
    h.printh()
