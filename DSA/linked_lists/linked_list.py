from node import Node

class LinkedList:

    def __init__(self):
        self.head = Node()
    
    def append(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node


if __name__ == "__main__":
    l = LinkedList()
    l.append(10)
    l.append(20)
    l.append(30)
    l.append(50)
