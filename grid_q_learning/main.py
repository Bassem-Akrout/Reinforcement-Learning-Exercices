import json
from Shared.graph.graph import Graph
from Discounted_MDP.solver.bellman_solver import BellmanSolver
#from solver.bellman_solver import BellmanSolver
from input import grid_input # Load JSON data
from randompolicy import grid_input_random_policy
rows=4
cols=5
gamma=0.9
grid_input((rows,cols))
grid_input_random_policy((rows,cols))
with open("grid_game_input.json", "r") as file:
    data = json.load(file)

states_to_actions = data["states_to_actions"]
actions_to_resulting_states = data["actions_to_resulting_states"]

# Create the graph
graph = Graph(states_to_actions, actions_to_resulting_states)

# Define terminal states
terminal_states = []

# Solve the Bellman equations
solver = BellmanSolver(graph, terminal_states,gamma)
solver.solve_until_convergence(max_iterations= 1000)

# Get results
value_matrix, policy_matrix = solver.get_results()

# Print results


# Initialize a matrix to store the values
value_matrix_display = [[0 for _ in range(cols)] for _ in range(rows)]

# Fill the matrix with values from the value matrix
for state, value in value_matrix.items():
    r, c = map(int, state.strip("()").split(","))
    value_matrix_display[r][c] = round(value, 2)  # Round for cleaner display

# Print the matrix
print("\nValue Matrix (V):")
for row in value_matrix_display:
    print(" | ".join(f"{value:.2f}" for value in row))


# Initialize a matrix to store the actions
policy_matrix_display = [["" for _ in range(cols)] for _ in range(rows)]

# Fill the matrix with actions from the policy matrix
for state, action in policy_matrix.items():
    r, c = map(int, state.strip("()").split(","))
    try:
        policy_matrix_display[r][c] = action.split("_")[-1]
    except:
        policy_matrix_display[r][c] = action

# Print the matrix
print("\nPolicy Matrix (π):")
for row in policy_matrix_display:
    print(" | ".join(row))
