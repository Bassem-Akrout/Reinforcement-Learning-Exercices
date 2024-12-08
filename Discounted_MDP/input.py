import json
import math

def generate_mdp_input(reward_function="linear", p=0.8, output_file="mdp_input.json"):
    """
    Generate an MDP input with customizable reward functions.

    :param reward_function: The type of reward function to use ("linear", "quadratic", "cubic", "exponential").
    :param p: Probability of transitioning to (state + 1) % 10 for action B.
    :param output_file: The name of the JSON file to save the input.
    """
    # Define the state and action space
    states = list(range(11))  # States: 0 to 10
    actions = ["A", "B"]  # Actions: A, B

    # Map states to their state-specific actions
    states_to_actions = {state: [f"A{state}", f"B{state}"] for state in states}

    # Define transitions and rewards for each state-specific action
    actions_to_resulting_states = {}

    # Choose the reward function
    if reward_function == "linear":
        reward = lambda state: state
    elif reward_function == "quadratic":
        reward = lambda state: state**2
    elif reward_function == "cubic":
        reward = lambda state: state**3
    elif reward_function == "exponential":
        reward = lambda state: math.exp(state)
    else:
        raise ValueError("Invalid reward_function. Choose 'linear', 'quadratic', 'cubic', or 'exponential'.")

    # Action A_i: Go to state 0 with reward based on the selected function
    for state in states:
        actions_to_resulting_states[f"A{state}"] = {
            0: [1.0, reward(state)]  # Probability 1.0, reward depends on the function
        }

    # Action B_i: Probabilistic transitions
    for state in states:
        next_state = (state + 1) % 10

        # Initialize a dictionary to store aggregated transitions
        aggregated_transitions = {}

        # Add transition to (state + 1) % 10
        if next_state not in aggregated_transitions:
            aggregated_transitions[next_state] = [p, 0]  # [Probability, Reward]
        else:
            aggregated_transitions[next_state][0] += p  # Aggregate probability

        # Add transition to 0
        if 0 not in aggregated_transitions:
            aggregated_transitions[0] = [round(1 - p, 10), 0]
        else:
            aggregated_transitions[0][0] += round(1 - p, 10)  # Aggregate probability

        # Add the aggregated transitions to actions_to_resulting_states
        actions_to_resulting_states[f"B{state}"] = aggregated_transitions

    # Save the inputs in JSON format
    data = {
        "states_to_actions": states_to_actions,
        "actions_to_resulting_states": actions_to_resulting_states,
    }

    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)

    print(f"MDP input generated and saved to {output_file} with {reward_function} rewards.")


# Example usage
if __name__ == "__main__":
    # Generate an MDP input with cubic rewards
    generate_mdp_input(reward_function="cubic", p=0.8, output_file="mdp_input_cubic.json")

    # Generate an MDP input with linear rewards
    generate_mdp_input(reward_function="linear", p=0.8, output_file="mdp_input_linear.json")

    # Generate an MDP input with quadratic rewards
    generate_mdp_input(reward_function="quadratic", p=0.8, output_file="mdp_input_quadratic.json")

    # Generate an MDP input with exponential rewards
    generate_mdp_input(reward_function="exponential", p=0.8, output_file="mdp_input_exponential.json")
