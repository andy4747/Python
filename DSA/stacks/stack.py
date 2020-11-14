from typing import Any

class Node:
    def __init__(self, data:Any) -> None:
        self.prev:Node = None
        self.data:Any = data
        self.next:Node = None

class Stack:
    def __init__(self) -> None:
        self.head:Node = None

    def push(self, data:Any) -> None:
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.prev = self.head
            self.head.prev = None
            self.head.next = new_node
            self.head = new_node

    def top(self) -> Any:
        return self.head.data

    def pop(self) -> Any:
        self.head.next = 


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    for i in s:
        print(i)
