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

    def get_list(self):
        """
        returns all the items from linked list as an array
        """
        items = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            items.append(current_node.data)
        return items

    def index_of(self, item):
        """
        returns the index of an item,
        returns first instance if multiple are presented in list
        """
        len = -1
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            len += 1
            if current_node.data == item:
                return len
        raise ValueError("Item not in list.")

    def get(self, index):
        """
        returns the item from the specified index
        """
        length = -1
        if index >= self.length:
            raise IndexError("index out of bound")
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            length += 1
            if length == index:
                return current_node.data



if __name__ == "__main__":
    l = LinkedList()
    l.append(0)
    l.append(10)
    l.append(20)
    l.append(30)
    l.append(40)
    l.append(50)
    l.append(60)
    l.append(70)
    l.append(80)
    l.append(90)
    print(l.length)
    l.display()
    print(l.get_list())
    print(l.index_of(90))
    print(l.get(0))
    l.clear()
    l.display()
