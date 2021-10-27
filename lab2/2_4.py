class Node:

    def __init__(self, key, price):
        if not isinstance(key, int) or not isinstance(price, (int, float)):
            raise Exception
        else:
            self.key = key
            self.price = price
            self.left = None
            self.right = None
            self.parent = None


class Tree:

    def __init__(self):
        self.root = None

    def add_node(self, key, price, node=None):

        if node is None:
            node = self.root

        if self.root is None:
            self.root = Node(key, price)

        else:
            if key == node.key:
                raise Exception
            if key < node.key:
                if node.left is None:
                    node.left = Node(key, price)
                    node.left.parent = node
                    return
                return self.add_node(key, price, node=node.left)
            else:
                if node.right is None:
                    node.right = Node(key, price)
                    node.right.parent = node
                    return
                return self.add_node(key, price, node=node.right)

    def search(self, key, node=None):

        if node is None:
            node = self.root

        if node.key == key:
            return node.price

        elif key < node.key and node.left is not None:
            return self.search(key, node=node.left)

        elif key > node.key and node.right is not None:
            return self.search(key, node=node.right)

        else:
            return None


try:
    t = Tree()
    t.add_node(10, 2)
    t.add_node(13, 3)
    t.add_node(14, 4)
    t.add_node(8, 8)
    t.add_node(9, 9)
    t.add_node(7, 7)
    t.add_node(11, 1)
    print(t.search(7))
except Exception:
    print('Error!')
