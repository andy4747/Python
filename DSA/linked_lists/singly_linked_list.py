class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __iter__(self) -> None:
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __len__(self) -> int:
        return len(tuple(iter(self)))

    def __repr__(self) -> str:
        return "=>".join([str(item) for item in self])

    def __getitem__(self, index:int) -> Node:
        if not 0 <= index <= len(self):
            raise IndexError('list index out of range')
        
        for i, node in enumerate(self):
            if i ==  index:
                return node

    def __setitem__(self, index:int, data) -> None:
        if not 0 <= index <= len(self):
            raise IndexError("list index out of range")
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        current_node.data = data



    def insert_at(self, index:int, data) -> None:
        if not 0 <= index <= len(self):
            raise IndexError("list index out of range")
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node

    def append(self, data) -> None:
        self.insert_at(len(self), data)

    def prepend(self, data) -> None:
        self.insert_at(0, data)

    def is_empty(self):
        return len(self) == 0


if __name__ == "__main__":
    l = LinkedList()
    l.append(10)
    l.append(20)
    l.append(30)
    print(l[1])
    print(l)
    del l
    # l.prepend(40)
    # l.prepend(50)
    # # print(len(l))
    # l.insert_at(len(l),100)
    # for i in l:
    #     print(i)
    # # print(l[0])
    # print(l.test().data)
