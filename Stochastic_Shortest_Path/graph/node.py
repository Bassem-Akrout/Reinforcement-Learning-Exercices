class Node:
    """
    Represents a node (state) in the graph, with its possible actions.
    """
    def __init__(self, name, actions=None):
        self.name = name
        self.actions = actions if actions else []  # List of Action objects

    def add_action(self, action):
        self.actions.append(action)

    def __str__(self):
        actions_str = ", ".join(str(a) for a in self.actions)
        return f"Node(name={self.name}, actions=[{actions_str}])"
