class Node():
    def __init__(self, data):
        self.right = None
        self.sibling = None
        self.left = None
        self.data = data

def linksibs(node):
    if node == None:
        return
    if node.left:
        node.left.sibling = node.right
    if node.right:
        if node.sibling:
            node.right.sibling = node.sibling.left
        else:
            node.right.sibling = None
    linksibs(node.left)
    linksibs(node.right)

def main():
    root = Node(10)
    root.sibling = None
    #creating a tree
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)

    linksibs(root)

    print root.sibling
    print root.left.sibling.data
    print root.right.sibling
    print root.left.left.sibling

if __name__ == '__main__':
    main()