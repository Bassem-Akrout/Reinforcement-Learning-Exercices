import json

from input import generate_mdp_input
from solver.bellman_solver import BellmanSolver

from Shared.graph.graph import Graph

# Step 1: Generate the input JSON dynamically
reward_function = "cubic"  # Choose between "linear", "quadratic", "cubic" ,"exponential"
generate_mdp_input(reward_function=reward_function, p=1 , output_file="mdp_input.json")

# Step 2: Load the generated JSON data
with open("mdp_input.json", "r") as file:
    data = json.load(file)

states_to_actions = data["states_to_actions"]
actions_to_resulting_states = data["actions_to_resulting_states"]

# Step 3: Create the graph
graph = Graph(states_to_actions, actions_to_resulting_states)

# Step 4: Define terminal states (if any)
terminal_states = []

# Step 5: Solve the Bellman equations
solver = BellmanSolver(graph, terminal_states, gamma=0.99)
solver.solve_until_convergence(tolerance=1e-12, max_iterations=100000)

# Step 6: Get and print results
value_matrix, policy_matrix = solver.get_results()

print("\nValue Matrix (V):")
for state, value in value_matrix.items():
    print(f"{state}: {value}")

print("\nPolicy Matrix (π):")
for state, action in policy_matrix.items():
    print(f"{state}: {action}")
