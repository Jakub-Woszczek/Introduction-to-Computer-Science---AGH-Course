# Zadanie 4. Proszę napisać funkcję, która dla podanej listy odsyłaczowej
# odwraca kolejność jej elementów

class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next


c = Node(3)
b = Node(2,c)
a = Node(1,b)
g = Node(None,a)

def print_list(head):
    print('GUARDIAN -> ', end='')
    while head != None:
        print(str(head.val) + ' -> ', end='')
        head = head.next
    print('KONIEC')

def reverse(p):
    if p.next == None:
        return p , p
    rev_start , rev_end = reverse(p.next)
    p.next = None
    rev_end.next = p
    return rev_start, p

print_list(reverse(g)[0])
