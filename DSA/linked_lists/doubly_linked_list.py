class Node:
    def __init__(self, data) -> None:
        self.prev = None
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self) -> None:
        current_node = self.head
        while current_node:
            yield current_node.data
            current_node = current_node.next

    def __len__(self) -> int:
        return len(tuple(iter(self)))

    def __str__(self) -> str:
        return "-->".join([str(i) for i in self])

    def insert_at(self, index:int, data) -> None:
        if not 0 <= index <= len(self):
            raise IndexError("list index out of range")
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        elif index == 0:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        elif len(self) == index:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            new_node.prev = current_node
            new_node.next = current_node.next
            current_node.next = new_node

    def append(self, value) -> None:
        self.insert_at(len(self), value)

    def delete_at(self, index:int) -> Node:
        if not 0 <= index <= len(self):
            raise IndexError("list index out of range")
        current_node = self.head
        if len(self) == 1:
            self.head = self.tail = None
        elif index == 0:
            self.head = self.head.prev
            self.head.prev = None
        elif index == len(self) - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            for _ in range(index):
                current_node = current_node.next
            current_node.next.prev = current_node.prev
            current_node.prev.next = current_node.next
        return current_node.data
    
    def remove_tail(self):
        self.delete_at(len(self) - 1)

    def remove_head(self):
        self.delete_at(0)

    def is_empty(self) -> bool:
        return len(self) == 0


if __name__ == "__main__":
    l = LinkedList()
    l.append(10)
    l.append(20)
    l.append(30)
    l.delete_at(len(l) - 1)
    for i in l:
        print(i)
