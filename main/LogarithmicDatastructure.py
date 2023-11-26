from AVLTree import AVLTree

class LogarithmicDatastructure:
    def __init__(self):
        self.avl_tree = AVLTree()  # AVL-Baumimplementierung oder eine andere balancierte Suchbaumstruktur

    def insert(self, key, value):
        self.avl_tree.insert(key, value)

    def get(self, key):
        node = self.avl_tree.find(key)
        return node.value if node else None

    def get_k_possible_suggestions(self, input_string, k):
        suggestions, searched_nodes = self.avl_tree.find_most_likely_ngrams(input_string)
        return suggestions, searched_nodes