class Transition:
    """
    Represents a transition resulting from an action.
    """
    def __init__(self, state, probability, cost):
        self.state = state
        self.probability = probability
        self.cost = cost

    def __str__(self):
        return f"Transition(state={self.state}, probability={self.probability}, cost={self.cost})"


class Action:
    """
    Represents an action from a node, including the resulting transitions.
    """
    def __init__(self, name, transitions):
        self.name = name
        self.transitions = [
            Transition(state, prob_cost[0], prob_cost[1]) for state, prob_cost in transitions
        ]  # Properly unpack nested lists  # Create Transition objects
        self.validate_probabilities()

    def validate_probabilities(self):
        total_probability = sum(t.probability for t in self.transitions)
        if abs(total_probability - 1.0) > 1e-6:
            raise ValueError(
                f"Invalid probabilities for action '{self.name}': sum is {total_probability}, expected 1.0"
            )

    def __str__(self):
        transitions_str = ", ".join(str(t) for t in self.transitions)
        return f"Action(name={self.name}, transitions=[{transitions_str}])"