class LL:
    def __init__(self,value):
        self.val = value
        # self.first = None
        self.last = None
        self.next = None

# L6 = LL(1)
# L6.first
# L6.last

# print(L6.first,L6.last)

node1 = LL(5)
node2 = LL(10)
node3 = LL(15)

node1.next = node2
node2.next = node3

cur_noode = node1
while cur_noode is not None:
    print(cur_noode.val)
    cur_noode = cur_noode.next



def add_nood(first,val):
    new_noode = LL(val)
    new_noode.next = first
    return new_noode

node1 = add_nood(node1,2)

def print_noodsy(Nood_1):
    cur_noode = Nood_1
    while cur_noode is not None:
        print(cur_noode.val)
        cur_noode = cur_noode.next

print_noodsy(node1)