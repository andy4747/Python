from node import Node

class LinkedList:

    def __init__(self):
        self.head = None
        self.current_node = None

    def build_from_list(self, array):
        self.head_value = array[0]
        current_node = Node(self.head_value)

        for index, value in enumerate(array[1:], 1):
            print(current_node)
            current_node.next = Node(value)
            current_node = current_node.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.build_from_list([10,20,30,40,50,60])
