class BellmanSolver:
    def __init__(self, graph, terminal_states):
        """
        :param graph: Graph object containing nodes and actions.
        :param terminal_states: List of terminal state names where V(s) = 0.
        """
        self.graph = graph
        self.terminal_states = set(terminal_states)
        self.value_matrix = {
            node_name: (0 if node_name in terminal_states else float('inf'))
            for node_name in graph.nodes.keys()
        }
        self.policy_matrix = {node_name: None for node_name in graph.nodes.keys()}

    def solve(self, iterations=100):
        """
        Solve the Bellman equations iteratively with a fixed number of iterations.
        :param iterations: Number of iterations for convergence.
        """
        for _ in range(iterations):
            self._update_values()

    def solve_until_convergence(self, tolerance=1e-6, max_iterations=1000,debug=False):
        """
        Solve the Bellman equations until the values stabilize within a tolerance.
        :param tolerance: The maximum allowable relative change for convergence.
        :param max_iterations: A cap on the number of iterations to prevent infinite loops.
        """
        for iteration in range(max_iterations):
            old_values = self.value_matrix.copy()  # Keep a copy of previous values
            self._update_values()

            # Debugging: Print old and new values
            if debug:
                print(f"Iteration {iteration + 1}")
                print("Old Values:", old_values)
                print("New Values:", self.value_matrix)

            # Check convergence
            max_relative_change = 0
            for state, new_value in self.value_matrix.items():
                old_value = old_values[state]

                if old_value == new_value:
                    # Skip comparison if there is no change
                    continue

                if old_value == float('inf'):
                    # If old value was infinite, assume full change
                    relative_change = 1.0
                elif old_value == 0:
                    # If old value was zero, check absolute change
                    relative_change = abs(new_value)
                else:
                    # Normal relative change calculation
                    relative_change = abs(new_value - old_value) / abs(old_value)

                # Debugging: Print relative change for each state
                print(f"State {state}: Relative Change = {relative_change}")

                max_relative_change = max(max_relative_change, relative_change)

            print(f"Max Relative Change = {max_relative_change}")

            if max_relative_change < tolerance:
                print(f"Converged after {iteration + 1} iterations with tolerance {tolerance}.")
                break
        else:
            print(f"Reached maximum iterations ({max_iterations}) without full convergence.")
    def _update_values(self):
        """
        Perform a single update of the value and policy matrices using Bellman equations.
        """
        for node_name, node in self.graph.nodes.items():
            if node_name in self.terminal_states:
                continue

            min_cost = float('inf')
            best_action = None

            for action in node.actions:
                expected_cost = 0
                for transition in action.transitions:
                    expected_cost += transition.probability * (
                        transition.cost + self.value_matrix[transition.state]
                    )

                if expected_cost < min_cost:
                    min_cost = expected_cost
                    best_action = action.name

            self.value_matrix[node_name] = min_cost
            self.policy_matrix[node_name] = best_action

    def get_results(self):
        """
        Get the computed value and policy matrices.
        """
        return self.value_matrix, self.policy_matrix
