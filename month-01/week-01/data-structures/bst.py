from collections import deque


class Node:
    """
    A single unit in a BST
    Provides a value and access to both it's child nodes
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    A graph that organizes nodes based on their binary relationship
    with their parent, left being smaller than the parent and right 
    being greater than the parent
    """
    def __init__(self):
        self.length = 0
        self.root = None

    def insert(self, nodeVal) -> None:
        """
            Insert a value into the BST

            Check if tree exists, if not set the value as the root node (initialization).
            If tree exists, compare the value with the root node, if its
            smaller, descend down the left, otherwise go right. Repeat this until you 
            reach a None node and set it to be the new node

            Args:
                nodeVal: Value to be inserted in BST
            Examples:
                >>> bst = BinarySearchTree()
                >>> bst.insert(5)
                >>> bst.insert(8)
        """
        node = Node(nodeVal)
        if self.root is None:
            self.root = node
            self.length += 1
            return
        currNode = self.root
        while True:
            if nodeVal < currNode.val:
                if currNode.left is None:
                    currNode.left = node
                    self.length += 1
                    return
                currNode = currNode.left
            elif nodeVal > currNode.val:
                if currNode.right is None:
                    currNode.right = node
                    self.length += 1
                    return
                currNode = currNode.right
            else:
                return

    def search(self, nodeVal) -> bool:
        """
            Search for a value in the BST

            Check to see if their exists a node with this value

            Args:
                nodeVal: Value in query
            Returns:
                bool: True if node exists, False otherwise
            Examples:
                >>> bst = BinarySearchTree()
                >>> bst.insert(5)
                >>> bst.insert(8)
                >>> bst.search(5)
        """
        if self.root is None:
            return False
        currNode = self.root
        while True:
            if nodeVal < currNode.value:
                if currNode.left is None:
                    return False
                currNode = currNode.left
            elif nodeVal > currNode.value:
                if currNode.right is None:
                    return False
                currNode = currNode.right
            else:
                return True
            

    def inOrder(self, node) -> None:
        """
            DFS traversal where we initially move from the lowest node 
            on the BST, and traverse our way back upward, checking
            each parent's sibling branch along the way

            Args:
                node: Root Node of BST

            Examples:
                >>> bst = BinarySearchTree()
                >>> bst.insert(5)
                >>> bst.insert(6)
                >>> bst.inOrder(bst.root)
        """
    
        if node is None:
            return
        self.inOrder(node.left)
        print(node)
        self.inOrder(node.right)

        
    def preOrder(self, node: Node) -> None:
        """
            DFS traversal where we initially visit the node itself, then 
            traverse down the left subtree, and finally traverse down the right subtree

            Args:
                node: Root Node of BST

            Examples:
                >>> bst = BinarySearchTree()
                >>> bst.insert(5)
                >>> bst.insert(6)
                >>> bst.preOrder(bst.root)
     """    
        if node is None:
            return
        else:
            print(node)
            self.preOrder(node.left)
            self.preOrder(node.right)
        

    def postOrder(self, node: Node) -> None:
        """
            DFS traversal where we traverse its left subtree first,
            then its right subtree, and finally visit the node itself

            Args:
                node: Root Node of BST

            Examples:
                >>> bst = BinarySearchTree()
                >>> bst.insert(5)
                >>> bst.insert(6)
                >>> bst.postOrder(bst.root)
     """    
        if node is None:
            return
        else:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node)    




    def BFS(self, node) -> None: 
        q = deque([node])
        li = []
        while len(q) != 0:
            node = q.popLeft()
            li.append(node)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        print(li)

    def DFS(self, node) -> None:
        q = deque([node])
        li = []
        while len(q) != 0:
            node = q.pop()
            li.append(node)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        print(li)

    def Delete(self,  nodeVal) -> bool:
        """
            Delete a value from the BST

            Check to see if there is a tree. If not
            return False. If yes, check to see if the node being 
            dleted follows into these three cases:
            1. Node has no children, simply remove the node
            2. Node has one child, remove the node and replace it with its child
            3. Node has two children
                a. Find the successor of the node (smallest node in the right subtree)
                b. Replace the value of the node with the successor's value
                c. Delete the successor node from the right subtree
            
            Args:
                nodeVal: Value to be deleted from the BST
            Returns:
                bool: True if node was successfully deleted, False otherwise
            Examples:
                >>> bst = BinarySearchTree()
                >>> bst.insert(5)
                >>> bst.insert(6)
                >>> bst.Delete(5)

        """
        if self.root is None:
            return False
        parent = None
        currNode = self.root
        while currNode is not None:
            if nodeVal < currNode.value:
                parent = currNode
                currNode = currNode.left
            elif nodeVal > currNode.value:
                parent = currNode
                currNode = currNode.right
        if currNode is None:
            return False
        
        if currNode.left is None or currNode.right is None:
            child = currNode.left if currNode.right is None else currNode.right
            if parent is None:
                self.root = child
            elif parent.left == currNode:
                parent.left = child
            else:
                parent.right = child
        else:
            successorParent = currNode
            successor = currNode.right

            while successor.left is not None:
                successorParent = successor
                successor = successor.left
            
            currNode.value = successor.value
            if successorParent.left == successor:
                successorParent.left = successor.right
            else:
                successorParent.right = successor.right
        self.length -= 1
        return True
        