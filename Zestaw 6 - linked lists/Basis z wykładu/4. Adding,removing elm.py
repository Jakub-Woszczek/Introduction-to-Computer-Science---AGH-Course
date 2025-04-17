class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:

                print(n.data,"--->",end=" ")
                n = n.ref

    def add_begin(self,data):
        new_noode = Node(data)
        new_noode.ref = self.head
        self.head = new_noode

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node





LL1 = LinkedList()
for bruh in range(1,11):

    LL1.add_end(bruh)


LL1.add_end(4)
LL1.add_begin(3)
LL1.print_LL()