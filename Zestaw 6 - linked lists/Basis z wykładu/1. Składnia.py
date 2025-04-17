class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

def print_noodes_rec(node):
    if node is None:
        return
    print(node.val)
    print_noodes_rec(node.next)

# Tworzymy węzły
node1 = Node(5)
node2 = Node(10)
node3 = Node(15)

# Ustawiamy połączenia między węzłami
node1.next = node2
node2.next = node3

# Przechodzimy przez listę i wyświetlamy wartości
current_node = node1
while current_node is not None:
    print(current_node.val)
    current_node = current_node.next
print(current_node)

print_noodes_rec(node1)