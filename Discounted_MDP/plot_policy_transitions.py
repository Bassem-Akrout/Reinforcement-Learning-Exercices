import matplotlib.pyplot as plt
import numpy as np
import json
from input import generate_mdp_input
from solver.bellman_solver import BellmanSolver
from Shared.graph.graph import Graph

# Parameters for the plot
gammaa = 0.99
p_values = np.linspace(0, 1, 500)
state_count = 11

# Store results for plotting
policy_decisions = []

for p in p_values:
    print(p)
    # Generate the MDP input for the current p value
    generate_mdp_input(reward_function="exponential", p=p, output_file="mdp_input.json")
    
    # Load the generated JSON data
    with open("mdp_input.json", "r") as file:
        data = json.load(file)

    states_to_actions = data["states_to_actions"]
    actions_to_resulting_states = data["actions_to_resulting_states"]

    # Create the graph
    graph = Graph(states_to_actions, actions_to_resulting_states)

    # Define terminal states (none for this case)
    terminal_states = []

    # Solve the Bellman equations
    solver = BellmanSolver(graph, terminal_states, gammaa)
    solver.solve_until_convergence(tolerance=1e-12, max_iterations=10000)

    # Get the policy for this p value
    _, policy_matrix = solver.get_results()
    #print(policy_matrix)
    policy_decisions.append([policy_matrix[str(state)] for state in range(state_count)])

# Convert policy decisions to numeric for plotting
policy_numeric = [[1 if action.startswith('B') else 0 for action in policy] for policy in policy_decisions]

# Plot the results
plt.figure(figsize=(10, 6))
for state in range(state_count):
    plt.plot(p_values, [policy[state] for policy in policy_numeric], label=f"State {state}")

plt.title("Policy Decisions for States as p Varies (Exponential Rewards, γ=0.7)")
plt.xlabel("Probability (p)")
plt.ylabel("Action (0 = A, 1 = B)")
plt.legend(title="State")
plt.grid(True)
plt.show()
