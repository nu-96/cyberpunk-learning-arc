class Node:
   """
   A single unit in a linked structure
   Holds a value and points to the next and prev nodes
   """
   def __init__(self, value):
        self.value = value
        self.nnext = None
        self.nprev = None

class LinkedList:
    """
    A sequential chain of Nodes
    Supports insertion, traversal and search
    """
    def __init__(self, *nodes):
        self.nlast = None
        self.length = 0
        self.nhead = None

    def append(self, value: int):
        """

        Insert value into the linked-list

        Checks to see if there is a tree, if no, 
        set the current value as the head and end 
        of tree. If yes, add the value to the end
        of the tree

        Args: 
            value: The integer to insert

        Example:
            >>> llist = LinkedList()
            >>> llist.insert(5)
            >>> llist.insert(3)
        
        """
        node = Node(value)
        if (self.nlast is None):
            self.nlast = node
            self.nhead = node
        else:
            node.nprev = self.nlast
            self.nlast.nnext = node
            self.nlast = node
        self.length = self.length + 1

    def delete(self, index):
        """
            Deletes a value from the linked-list

            Checks to see if there is a tree. If yes,
            and index is 0, remove the old head and update 
            the linked-list's new head. If yes and index is 
            < len(linked-list) - 1 > (last element in list),
            remove the last, and update the list with a new last node.
            Otherwise, just remove the element from the list and update 
            it's previous and next nodes

            Args:
                index: index of deletion
            
            Examples:
                >>> llist = LinkedList()
                >>> llist.insert(5)
                >>> llist.delete(0)

        """
        if (self.nlast is None):
            pass
        else:
            if (index < self.length):
                if (index == 0):
                   self.nhead = self.nhead.nnext
                   if (self.nhead is not None):
                       self.nhead.nprev = None
                   self.length -= 1
                else:
                    if (index == self.length - 1):
                        self.nlast = self.nlast.nprev
                        if (self.nlast is not None):
                            self.nlast.nnext = None
                        self.length -= 1
                    else:
                        val = self.nlast
                        for i in range(self.length - index - 1):
                            val = val.nprev
                        val.nprev.nnext = val.nnext
                        val.nnext.nprev = val.nprev
                        self.length -= 1
    def search(self, index) -> int:
        """
        Search for the value at the index

        Check to see if tree exists, if so traverse the list
        until you find the index and print that value

        Args:
            index: index of value in list
        
        Returns:
            int: value at that index

        Examples:
            >>> llist = LinkedList()
            >>> llist.insert(5)
            >>> llist.search(0)
        """
        if (self.nhead is None):
            pass
        else:
            val = self.nlast
            if index != 0:
                for i in range(index):
                    val = val.nprev
            else:
                val = self.nhead
            return val.value

    def __repr__(self):
        """
        Print Function
        """
        val = self.nhead
        string = ''
        for i in range (self.length):
            if (val.nnext is None):
                string = f"{string}{val.value}"
            else:
                string = f"{string}{val.value} -> "
                val = val.nnext
        return string

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.delete(1)
print(ll)