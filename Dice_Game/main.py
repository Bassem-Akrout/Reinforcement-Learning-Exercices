import json
from Shared.graph.graph import Graph
from Discounted_MDP.solver.bellman_solver import BellmanSolver
#from solver.bellman_solver import BellmanSolver
from input import dice_game_input # Load JSON data

d=3

dice_game_input(d)
with open("dice_game_input.json", "r") as file:
    data = json.load(file)

states_to_actions = data["states_to_actions"]
actions_to_resulting_states = data["actions_to_resulting_states"]

# Create the graph
graph = Graph(states_to_actions, actions_to_resulting_states)

# Define terminal states
terminal_states = data["terminal_states"]

# Solve the Bellman equations
solver = BellmanSolver(graph, terminal_states,1)
solver.solve_until_convergence()

# Get results
value_matrix, policy_matrix = solver.get_results()

# Print results
print("Value Matrix (V):")
for state, value in value_matrix.items():
    print(f"{state}: {value}")

print("\nPolicy Matrix (π):")
for state, action in policy_matrix.items():
    try:print(f"{state}: {action[-1]}") 
    except:print(f"{state}: {action}")
