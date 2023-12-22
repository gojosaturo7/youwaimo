class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

def alpha_beta_pruning(node, alpha, beta, maximizing_player):
    if not node.children:
        return node.value

    if maximizing_player:
        value = float('-inf')
        for child in node.children:
            value = max(value, alpha_beta_pruning(child, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value
    else:
        value = float('inf')
        for child in node.children:
            value = min(value, alpha_beta_pruning(child, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value

tree = Node(3, [
    Node(5, [
        Node(9),
        Node(12),
        Node(8)
    ]),
    Node(2, [
        Node(7),
        Node(10),
        Node(6)
    ]),
    Node(8, [
        Node(6),
        Node(1),
        Node(11)
    ])
])

result = alpha_beta_pruning(tree, float('-inf'), float('inf'), True)
print("Optimal value:", result)
