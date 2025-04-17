class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def print_list(head):
    while head != None:
        print(str(head.val) + ' -> ', end='')
        head = head.next
    print('KONIEC')

def remove_element(p, to_del):
    prev = None
    start = p

    while p != None:
        if p.val == to_del:
            if prev == None:
                return p.next
            else:
                prev.next = prev.next.next
                return start
        prev = p
        p = p.next

    return start

def add_el(p,to_add):
    start = p
    prev = None
    while p != None:
        prev = p
        p = p.next

    if prev == None:
        return Node(to_add)

    prev.next = Node(to_add)
    return start


e = Node(5)
d = Node(4,e)
c = Node(3,d)
b = Node(2,c)
a = Node(1,b)
guardian = Node(a)
print_list(guardian)

# remove_element(a,1)
for i in range(6,10):
    add_el(a,i)
print_list(a)

