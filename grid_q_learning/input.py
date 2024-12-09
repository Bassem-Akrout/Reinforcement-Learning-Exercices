import json

def grid_input(grid_size=(4,5), gray_cells={(3, 0): [(1, 1), 4], (2, 2): [(0, 2), 2]}, output_file="grid_game_input.json"):
    """
    Generate the states, actions, and transitions for the grid problem and save them to a JSON file.

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
            states_to_actions[str(state)] = [f"{state}_GRAY"]
            actions_to_resulting_states[f"{state}_GRAY"] = {str(gray_cells[state][0]):[1.0,gray_cells[state][1]]}
        else:
            #states_to_actions[state]=[f"{state}_{direction}" for direction in directions.keys()]
            #for direction in directions.keys():
            #    actions_to_resulting_states[f"{state}_{direction}"]=[]
            #           
            # White cells: Four possible movements
            actions = []
            for action, (dr, dc) in directions.items():
                actions.append(f"{state}_{action}")
                next_r, next_c = state[0] + dr, state[1] + dc

                if 0 <= next_r < rows and 0 <= next_c < cols:
                    # Valid move within grid bounds
                    next_state = (next_r, next_c)
                    actions_to_resulting_states[f"{state}_{action}"] = {str(next_state): [1.0, 0]}
                else:
                    # Invalid move: Stay in the same position with a penalty
                    actions_to_resulting_states[f"{state}_{action}"] = {str(state): [1.0, -1]}
            states_to_actions[str(state)] = actions
    


    """
        for state in states:
            if state in gray_cells:
                # Gray cells: Direct transition to destination with a reward
                destination, reward = gray_cells[state]
                actions_to_resulting_states[f"{state}_GRAY"] = {destination: [1.0, reward]}
                states_to_actions[state] = [f"{state}_GRAY"]
            else:
                # White cells: Four possible movements
                actions = []
                for action, (dr, dc) in directions.items():
                    actions.append(f"{state}_{action}")
                    next_r, next_c = state[0] + dr, state[1] + dc

                    if 0 <= next_r < rows and 0 <= next_c < cols:
                        # Valid move within grid bounds
                        next_state = (next_r, next_c)
                        actions_to_resulting_states[f"{state}_{action}"] = {next_state: [1.0, 0]}
                    else:
                        # Invalid move: Stay in the same position with a penalty
                        actions_to_resulting_states[f"{state}_{action}"] = {state: [1.0, -1]}

                states_to_actions[state] = actions
    """
    # Save states, actions, and transitions to JSON
    data = {
        "states": states,
        "states_to_actions": states_to_actions,
        "actions_to_resulting_states": actions_to_resulting_states,
    }
    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Grid input generated and saved to {output_file}.")

if __name__ == "__main__":
    grid_input()
