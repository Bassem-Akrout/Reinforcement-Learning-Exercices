import json
from graph.graph import Graph
from solver.bellman_solver import BellmanSolver

# Load JSON data
with open("graph.json", "r") as file:
    data = json.load(file)

states_to_actions = data["states_to_actions"]
actions_to_resulting_states = data["actions_to_resulting_states"]

# Create the graph
graph = Graph(states_to_actions, actions_to_resulting_states)

# Define terminal states
terminal_states = ["P"]

# Solve the Bellman equations
solver = BellmanSolver(graph, terminal_states)
solver.solve_until_convergence()

# Get results
value_matrix, policy_matrix = solver.get_results()

# Print results
print("Value Matrix (V):")
for state, value in value_matrix.items():
    print(f"{state}: {value}")

print("\nPolicy Matrix (π):")
for state, action in policy_matrix.items():
    print(f"{state}: {action}")
