''' this is an implementaion of a sigly linked list '''

class SLL_NODE:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = SLL_NODE(value)
        if (self.head == None):
            self.head = node
        else:
            curr = self.head
            while(curr.next != None):
                curr = curr.next
            curr.next = node

    def insert_at_head(self, value):
        node = SLL_NODE(value)
        if (self.head == None):
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def printl(self):
        if (self.head != None):
            curr = self.head
            print("[ "),
            while(curr):
                print(curr.value),
                curr = curr.next
            print(" ]")
        else:
            print("List is empty")

    def search(self, value):
        if (self.head != None):
            i = 0
            curr = self.head
            while(curr):
                if (curr.value == value):
                    print ("%d is at index %d"%(value, i))
                    return i
                else:
                    curr = curr.next
                    i = i + 1
            print("%d is not found in the List"%(value))
        else:
            print ("List is empty")

    def delete(self, value):
        if (self.head == None):
            print("List is empty")
        else:
            curr = self.head
            prev = None
            while (curr):
                if (curr.value == value):
                    if (prev != None):
                        prev.next = curr.next
                        return
                    else:
                        self.head = curr.next
                        return
                else:
                    prev = curr
                    curr = curr.next
            print("Could not find %d in list"%(value))

    def length(self):
        if (self.head == None):
            return 0
        else:
            curr = self.head
            count = 0
            while(curr):
                count  = count + 1
                curr = curr.next
            return count

    def swap_nodes(self, x, y):
        # function to swap the nodes with value x and y without
        # swappning the values
        if (self.head == None):
            print ("Can't swap. List is empty")
            return
        elif (x == y):
            print ("Swapnning the same values. Nothing to do")
            return
        else:
            curr = self.head
            prevx = prevy = None
            xnode = ynode = None
            while(curr):
                if ((xnode == None) and (curr.value == x)):
                    xnode = curr
                if ((ynode == None) and (curr.value == y)):
                    ynode = curr
                if (xnode == None):
                    prevx = curr
                if (ynode == None):
                    prevy = curr
                if (xnode and ynode):
                    break
                else:
                    curr = curr.next
            if ((xnode is None) or (ynode is None)):
                print ("Either of the node is not present. ")
                return
            if (prevx == None):
                # xnode is head of the ll
                self.head = ynode
            else:
                prevx.next = ynode
            if (prevy == None):
                # ynode is head of the ll
                self.head = xnode
            else:
                prevy.next = xnode
            # swap the next nodes
            temp = ynode.next
            ynode.next = xnode.next
            xnode.next = temp
        self.printl()

    def reverse(self):
        if (self.head == None):
            print ("Linked list is empty")
            return
        else:
            prev = None
            curr = self.head
            next = None
            while(curr != None):
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            self.head = prev
            self.printl()

    def rotate(self, k):
        if (self.head == None):
            print ("Linked list is empty. Nothing to rotate")
            return
        if (k == 0):
            return
        n = self.length()
        if (k >= n):
            print ("rotation lenght is greater than the length of the linked list")
            return
        i = 0
        curr = self.head
        prev = None
        while(curr != None):
            if (i == k):
                break
            i = i + 1
            prev = curr
            curr = curr.next
        if (prev != None):
            prev.next = None
        new_head = curr
        while (curr.next != None):
            curr =  curr.next
        curr.next = self.head
        self.head = new_head
        self.printl()


    def get_decimal_number_from_ll(self):
        negative = False
        if (self.head == None):
            print ("List is empty")
            return 0
        else:
            if (self.head.value == '-'):
                negative = True
            if (negative):
                curr = self.head.next
            else:
                curr = self.head
            no = 0
            while (curr != None):
                no = no*10 + curr.value
                curr = curr.next
            if (negative):
                return (no * -1)
            else:
                return no

    def get_from_index(self, index):
        if (self.head is None):
            print("List is empty")
            return
        curr = self.head
        count = 0
        while(curr):
            if (count == index):
                return curr.value
            else:
                curr = curr.next
                count += 1
        print("Index %d is not present in the list"%(index))

    def get_middle_element(self):
        if (self.head is None):
            return None
        if (self.head.next is None):
            return self.head.value
        slow = self.head
        fast = self.head
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        return slow.value



def add_two_numbers_represent_by_lls(l1, l2):
    if (l1 == None and l2 == None):
        print("Both lls are None")
    elif (l1 == None and l2 != None):
        l2.printl()
    elif (l1 != None and l2 == None):
        l1.printl()
    else:
        n1 = l1.get_decimal_number_from_ll()
        n2 = l2.get_decimal_number_from_ll()
        result = n1 + n2
        resll = SLL()
        if (result == 0):
            resll.insert(0)
        else:
            if (result < 0):
                resll.insert_at_head('-')
                result = -1 * result
            while(result != 0):
                no = result % 10
                resll.insert_at_head(no)
                result = (result - no) / 10
        resll.printl()

if __name__ == "__main__":
    '''l = SLL()
    for i in range(10):
        l.insert(i)
    l.printl()
    l.swap_nodes(5, 8)
    l.reverse()

    l1 = SLL()
    l2 = SLL()
    # first no is 356
    l1.insert('-')
    l1.insert(3)
    l1.insert(5)
    l1.insert(6)
    # second no is 484
    l2.insert(0)
    l2.insert(3)
    l2.insert(5)
    l2.insert(6)
    add_two_numbers_represent_by_lls(l1, l2)
    '''
    l = SLL()
    for i in range(4):
        l.insert(i+1)
    l.printl()
    #print(l.get_from_index(3))
    print(l.get_middle_element())
