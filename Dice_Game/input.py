import itertools
import json

def dice_game_input(d=3, output_file="dice_game_input.json"):
    """
    Generate the states, actions, and transitions for the dice game and save them to a JSON file.

    :param d: Number of faces on the dice.
    :param output_file: File to save the generated MDP input.
    """
    # Define special states
    terminal_states = ["L", "S", "-".join(map(str, range(1, d + 1)))]  # Loss, Stop, Final full sequence (e.g., "1-2-3-4" for d=4)

    # Generate all possible states (combinations of dice faces seen so far)
    all_states = []
    for r in range(1, d):  # Combinations of 1 to (d-1) dice faces
        for combination in itertools.combinations(range(1, d + 1), r):
            all_states.append("-".join(map(str, combination)))  # Use "-" as a delimiter

    # Add special states
    all_states.extend(terminal_states)

    # Map each state to its possible actions
    states_to_actions = {}
    actions_to_resulting_states = {}
    print(all_states)
    for state in all_states:
        if state in terminal_states:
            states_to_actions[state] = []  # No actions in terminal states (L, S, W)
            continue

        # Actions: Stop (S) or Roll (R)
        states_to_actions[state] = [state + "_S", state + "_R"]

        # Define transitions for Roll (R)
        if state not in terminal_states:
            current_faces = set(state.split("-"))  # Current set of observed faces
            available_faces = set(map(str, range(1, d + 1))) - current_faces  # Faces not yet rolled
            transitions = {}

            for face in available_faces:
                next_state = "-".join(sorted(current_faces | {face}, key=int))  # New state after rolling a unique face
                transitions[next_state] = [round(1 / d, 10), int(face)]  # [Probability, Reward (value of new face)]
            
            # Add transition to Loss (L) if a duplicate is rolled
            transitions["L"] = [round(len(current_faces) / d, 10), -sum(map(int, current_faces))]  # [Probability of duplicate roll, Negative Reward]

            actions_to_resulting_states[state + "_R"] = transitions

        # Define transitions for Stop (S)
        actions_to_resulting_states[state + "_S"] = {
            "S": [1.0, sum(map(int, state.split("-")))]  # Transition to Stop with total reward (sum of unique faces seen so far)
        }

    # Save states, actions, and transitions to JSON
    data = {
        "terminal_states": terminal_states,
        "states_to_actions": states_to_actions,
        "actions_to_resulting_states": actions_to_resulting_states,
    }
    
    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)
    
    print(f"MDP input generated and saved to {output_file}.")

if __name__ == "__main__":
    dice_game_input(d=3)
