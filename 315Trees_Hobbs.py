# Programming Assignment 2: Trees!
# Author: Rylee Hobbs
# Class: CS315
#Opens file and reads every line into a RandomInslist
file = open("testrandom.csv", "r")
text = file.readlines()
text.pop(0)
RandominsList = []
for i in range(len(text)):
    text[i] = text[i].rstrip("\n")
    RandominsList.append(int(text[i]))
print(RandominsList)

#Opens file and reads every line into a BadinsList
file = open("testBad.csv", "r")
text = file.readlines()
text.pop(0)
BadinsList = []
for i in range(len(text)):
    text[i] = text[i].rstrip("\n")
    BadinsList.append(int(text[i]))
print(BadinsList)

#Opens file and reads every line into a list
file = open("deleteNodes.csv", "r")
text = file.readlines()
text.pop(0)
deleteList = []
for i in range(len(text)):
    text[i] = text[i].rstrip("\n")
    deleteList.append(int(text[i]))
print(deleteList)

class Node:
    def __init__(x, key):
        x.left = None
        x.right = None
        x.key = key
        x.parent = None

def height(root):
        #check if empty
        if root is None:
            return 0
        leftHeight = height(root.left)
        rightHeight = height(root.right)

        #return max of the two traversals
        return max(leftHeight, rightHeight) + 1

class BST:
    def __init__(self):
        self.root = None
    
    # insert node
    def BSTinsert(T, z):
        y = None
        x = T.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        
        z.parent = y

        if y == None: #newly added node is root
            T.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z


    # delete node
    def BSTdelete(T, z):
        if z.left == None:
            T.transplant(z, z.right)

        elif z.right == None:
            T.transplant(z, z.left)

        else:
            y = T.tree_min(z.right)
            if y.parent != z:
                T.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            T.transplant(y, y.right)
            y.left = z.left
            y.left.parent = y

    # transplant function
    def transplant(T, u, v):
        if u.parent == None:
            T.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v != None:
            v.parent = u.parent
        
    """
        Tree-Search:
        x = node currently searching
        k = value we're looking for
    """
    def tree_search(x, k):
        if x == None or k == x.key:
            return x
        if k < x.key:
            return x.tree_search(x.left, k)
        else:
            return x.tree_search(x.right, k)

    # determine min
    def tree_min(x):
        
        while x.left != None:
            x = x.left
        return x

    #Determine max
    def tree_max(x):

        while x.right != None:
            x = x.right
        return x

    # in-order traversal
    def inorder_trav(T, x):
        if x != None:
            T.inorder_trav(x.left)
            print(x.key)
            T.inorder_trav(x.right)


#### Red-Black Tree ####
Red = 'Red'
Black = 'Black'

class RBNode:
    def __init__(x, key):
        x.left = None
        x.right = None
        x.parent = None
        x.key = key
        x.color = Red

class RBTree:
    def __init__(x):
        nil_node = RBNode(0)
        nil_node.color = Black
        x.NIL = nil_node
        x.root = x.NIL

    def RBinsert(T, z):
        y = T.NIL
        x = T.root

        while x != T.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y

        if y == T.NIL: #new node is root
            T.root = z

        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        z.left = T.NIL
        z.right = T.NIL
        
        T.RBinsert_fix(z)

    def RBinsert_fix(T, z):
        while z.parent.color == Red:
            if z.parent == z.parent.parent.left:

                y = z.parent.parent.right

                if y.color == Red: #case 1
                    z.parent.color = Black
                    y.color = Black
                    z.parent.parent.color = Red
                    z = z.parent.parent

                else:
                    if z == z.parent.right: #case2
                        z = z.parent
                        T.left_rotate(z)
                #case3
                z.parent.color = Black #made parent black
                z.parent.parent.color = Red #made parent red
                T.right_rotate(z.parent.parent)

            else: 
                y = z.parent.parent.left #uncle of z
                
                if y.color == Red:
                    z.parent.color = Black
                    y.color = Black
                    z.parent.parent.color = Red
                    z = z.parent.parent

                else: 
                    if z == z.parent.left:
                        z = z.parent #z parent is new z
                        T.right_rotate(z)

                    z.parent.color = Black
                    z.parent.parent.color = Red
                    T.left_rotate(z.parent.parent)
        T.root.color = Black

    # rotate left
    def left_rotate(T, x):
        y = x.right         # set y
        x.right = y.left    # turn x's right subtree into y's left subtree
        if y.left != T.NIL:
            y.left.parent = x
        y.parent = x.parent           # link x parent to y
        if x.parent == T.Nil:
            T.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x          # put x on y's left
        x.parent = y

    # rotate right
    def right_rotate(T, x):
        y = x.left         # set y
        x.left = y.right    # turn x's left subtree into y's right subtree
        if y.right != T.NIL:
            y.right.parent = x
        y.parent = x.parent           # link x parent to y
        
        if x.parent == T.NIL:
            T.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x          # put x on y's right
        x.parent = y

    def RBtransplant(T, u, v):
        if u.parent == T.NIL:
            T.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def RBMin(T, x):
        while x.left != T.NIL:
            x = x.left
        return x

    #Red-Black tree delete
    def RBdelete(T, z):
        y = z
        x = None
        y_original = y.color
        if z.left == T.NIL:
            x = z.right
            T.RBtransplant(z, z.right)

        elif z.right == T.NIL:
            x = z.left
            T.RBtransplant(z, z.left)

        else:
            y = T.RBMin(z.right)
            y_original = y.color
            x = y.right
            if y.parent == z:
                x.parent = z

            else: 
                T.RBtransplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            T.RBtransplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color

        if y_original == Black:
            T.RBdelete_fix(x)

    def RBdelete_fix(T, x):
        while x != T.root and x.color == Black:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == Red:
                    w.color = Black
                    x.parent.color = Red
                    T.left_rotate(x.parent)
                    w = x.parent.right

                if w.left.color == Black and w.right.color == Black:
                    w.color = Red
                    x = x.parent

                else:
                    if w.right.color == Black:
                        w.left.color = Black
                        w.color = Red
                        T.right_rotate(w)
                        w = x.parent.right

                    w.color = x.parent.color
                    x.parent.color = Black
                    w.right.color = Black
                    T.left_rotate(x.parent)
                    x = T.root
            else:    
                w = x.parent.left
                if w.color == Red:
                    w.color = Black
                    x.parent.color = Red
                    T.right_rotate(x.parent)
                    w = x.parent.left

                if w.right.color == Black and w.left.color == Black:
                    w.color = Red
                    x = x.parent

                else:
                    if w.left.color == Black:
                        w.right.color = Black
                        w.color = Red
                        T.left_rotate(w)
                        w = x.parent.left

                    w.color = x.parent.color
                    x.parent.color = Black
                    w.left.color = Black
                    T.right_rotate(x.parent)
                    x = T.root 
        x.color = Black
        def inorder(T, z):
            if z != T.NIL:
                inorder(T, z.left)
                print(z.key)
                inorder(T, z.right)

#### BST implementation for random insert ####
if __name__ == '__main__':
    t = BST()

    for i in range(len(RandominsList)):
        t.BSTinsert(Node(RandominsList[i]))

    print("In-order Traversal: \n", end = '')
    t.inorder_trav(t.root)

    print("Height of RandInsert tree: " + str(height(t.root)))

    #deleting nodes
    for i in range(len(deleteList)):
        print("/n Deleting Node %d", deleteList[i])
        t.BSTdelete(Node(deleteList[i]))

    print("Height of RandInsert tree after delete: " + str(height(t.root)))

    #### BST implementation for BadInsert ####
    for i in range(len(BadinsList)):
        t.BSTinsert(Node(BadinsList[i]))

    print("In-order Traversal: ", end = ' ')
    t.inorder_trav(t.root)

    print("Height of BadInserttree: " + str(height(t.root)))

    for i in range(len(deleteList)):
        print("/n Deleting Node %d", Node(deleteList[i]))
        t.BSTdelete(Node(deleteList[i]))
    print("Height of BadInsert tree after delete: " + str(height(t.root)))

    

    #### RBT implementation for RandInsert ####
    u = RBTree()
    for i in range(len(RandominsList)):
        u.RBinsert(RBNode(RandominsList[i]))

    print("In-order Traversal: ", end = ' ')
    u.inorder(u.root)

    print("Height of RandInsert RB-tree: " + str(height(u.root)))

    #deleting nodes
    for i in range(len(deleteList)):
     print("/n Deleting Node %d", deleteList[i])
     u.RBdelete(RBNode(deleteList[i]))

    print("Height of RandInsert RB-tree after delete: " + str(height(u.root)))

    #### RBT implementation for BadInsert ####
    for i in range(len(BadinsList)):
        u.RBinsert(RBNode(BadinsList[i]))

    print("In-order Traversal: ", end = '')
    u.inorder(u.root)

    print("Height of BadInsert RB-tree: " + str(height(u.root)))

    #deleting nodes
    for i in range(len(deleteList)):
        print("/n Deleting Node %d", deleteList[i])
        u.RBdelete(RBNode(deleteList[i]))
    print("Height of BadInsert RB-tree after delete: " + str(height(u.root)))


