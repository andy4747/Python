class Stack:
    
    def __init__(self):
        """
        Initializing a list for stacking
        """
        self.items = []
        
    def push(self, item):
        """
        Push the elements at the end of the list
        
        :return: None
        """
        
        self.items.append(item)
        
    def pop(self):
        """
        removes the item at the last index
        
        :return: None
        """
        self.items.pop()
        
        
    def peek(self):
        """
        returns the item at the last index
        
        :return: list[-1]
        """
        if self.items:
            return self.items[-1]
        else:
            return None
    
    def size(self):
        """
        returns the size of the stack
        
        :return: integer
        """
        return len(self.items)
    
    def is_empty(self):
        """
        checks if the list is empty or not
        
        :return: boolean
        """
        if self.items == []:
            return True
        else:
            return False
