class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None


if __name__ == "__main__":
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)

    node1.next = node2
    node2.next = node3
    node2.previous = node1
    node3.previous = node2

    print(f"node1: {node1}")
    print(f"node2: {node2}")
    print(f"node3: {node3}")

    print(f"node1.next: {node1.next}")
    print(f"node2.next: {node2.next}")
    print(f"node3.next: {node3.next}")

    print(f"node1.previous: {node1.previous}")
    print(f"node2.previous: {node2.previous}")
    print(f"node3.previous: {node3.previous}")
