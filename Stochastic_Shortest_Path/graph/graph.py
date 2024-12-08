from .node import Node
from .action import Action

class Graph:
    """
    Represents the entire graph, including nodes and actions.
    """
    def __init__(self, states_to_actions, actions_to_resulting_states):
        self.nodes = self._build_graph(states_to_actions, actions_to_resulting_states)

    def _build_graph(self, states_to_actions, actions_to_resulting_states):
        nodes = {}
        for state, action_names in states_to_actions.items():
            node = Node(name=state)
            for action_name in action_names:
                transitions = actions_to_resulting_states.get(action_name, {}).items()
                action = Action(name=action_name, transitions=transitions)
                node.add_action(action)
            nodes[state] = node
        return nodes

    def get_node(self, name):
        return self.nodes.get(name)

    def __str__(self):
        return "\n".join(str(node) for node in self.nodes.values())
