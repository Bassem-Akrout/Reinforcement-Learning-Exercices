import json

def grid_input_random_policy(grid_size=(4, 5), gray_cells={(3, 0): [(1, 1), 4], (2, 2): [(0, 2), 2]}, output_file="grid_game_random_policy.json"):
    """
    Generate the states, actions, and transitions for the grid problem under a random policy with a single action "Move (M)"
    and save them to a JSON file.

    :param grid_size: Tuple representing the grid dimensions (rows, columns).
    :param gray_cells: Dictionary where keys are positions of gray cells, and values are tuples of (destination, reward).
    :param output_file: File to save the generated MDP input.
    """
    rows, cols = grid_size
    states = []
    states_to_actions = {}
    actions_to_resulting_states = {}

    directions = {"UP": (-1, 0), "DOWN": (1, 0), "LEFT": (0, -1), "RIGHT": (0, 1)}

    # Generate all grid states
    for r in range(rows):
        for c in range(cols):
            states.append((r, c))

    for state in states:
        if state in gray_cells:
            # Gray cells: Only one action to transition directly
            states_to_actions[str(state)] = [f"{state}_GRAY"]
            actions_to_resulting_states[f"{state}_GRAY"] = {str(gray_cells[state][0]): [1.0, gray_cells[state][1]]}
        else:
            # White cells: Only one action "Move (M)"
            move_action = f"{state}_M"
            transitions = {}

            # Compute probabilities for moving in each direction
            total_directions = 0
            for action, (dr, dc) in directions.items():
                next_r, next_c = state[0] + dr, state[1] + dc
                if 0 <= next_r < rows and 0 <= next_c < cols:
                    next_state = (next_r, next_c)
                    transitions[str(next_state)] = transitions.get(str(next_state), 0) + 1
                    total_directions += 1
                else:
                    # Out of bounds, stay in the same position
                    transitions[str(state)] = transitions.get(str(state), 0) + 1
                    total_directions += 1

            # Normalize probabilities and assign rewards
            normalized_transitions = {
                state_key: [count / total_directions, 0 if state_key != str(state) else -1]
                for state_key, count in transitions.items()
            }

            # Add the "Move (M)" action
            states_to_actions[str(state)] = [move_action]
            actions_to_resulting_states[move_action] = normalized_transitions
            print(move_action,actions_to_resulting_states[move_action])

    # Save states, actions, and transitions to JSON
    data = {
        "states": states,
        "states_to_actions": states_to_actions,
        "actions_to_resulting_states": actions_to_resulting_states,
    }
    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Grid input with random policy generated and saved to {output_file}.")

if __name__ == "__main__":
    grid_input_random_policy()
