from node import Node

class LinkedList:

    def __init__(self):
        self.head = Node()
    
    def append(self, data):
        """
        adds item to the end of the list
        """
        new_node = Node(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node

    def display(self):
        """
        prints all the items in linked list
        """
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            print(current_node.data, end=" | ")
        print()

    @property
    def length(self):
        """
        returns the length of the linked list
        """
        current_node = self.head
        len = 0
        while current_node.next != None:
            current_node = current_node.next
            len += 1
        return len

if __name__ == "__main__":
    l = LinkedList()
    l.append(10)
    l.append(20)
    l.append(30)
    l.append(50)
    print(l.length)
    l.display()
