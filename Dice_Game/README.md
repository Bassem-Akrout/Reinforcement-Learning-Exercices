
# Dice Game - MDP Implementation

This repository contains an implementation of a Markov Decision Process (MDP) for a dice game. The goal is to determine the optimal policy and value function for maximizing expected rewards under the game’s rules.

---

## Problem Statement

The dice game involves:
- **State space**: Representing combinations of dice faces seen so far.
- **Action space**: Stop (`S`) or Roll (`R`).

### Game Rules:
1. Roll a dice with `d` faces up to `d` times.
2. After each roll, you can:
   - **Stop**: Earn the sum of unique values observed so far.
   - **Roll again**: If a new face is observed, it is added to the total; if a duplicate face is rolled, you lose and earn `0`.
3. Terminal states:
   - **Loss (`L`)**: Occurs when a duplicate is rolled.
   - **Stop (`S`)**: Occurs when the player chooses to stop.
   - **Win**: Reaching all `d` unique dice faces.

---

## Implementation Details

### Structure

```
Dice_Game/
├── input.py                   # Generates input data for the dice game (states, actions, transitions).
├── main.py                    # Main script to solve the MDP using Bellman equations.
└─── dice_game_input.json       # Generated MDP input file for the dice game.
```

### Key Components

1. **State Space**:
   - States represent combinations of dice faces observed so far, delimited by `-` (e.g., `1-2-3`).
   - Terminal terminal states: `L`, `S`, and `1-2-3-...-d` **(The win state)**.

2. **Actions**:
   - **Stop (`S`)**: Ends the game and returns the sum of observed faces.
   - **Roll (`R`)**: Rolls the dice for a new face.

3. **Transitions**:
   - Rolling a new face transitions to a new state with probability \(1/d\).
   - Rolling a duplicate face transitions to `L` .

4. **Reward Function**:
   - Stop: Sum of unique observed faces.
   - Roll: If a unique face is rolled, the reward is the value of the new face. If a duplicate face is rolled, a negative reward equal to the total reward accumulated for that sequence is applied (you lose what you previously won).

---

## Results

The value function (`V`) and policy (`π`) are computed using **value iteration**. The optimal policy determines whether to stop or roll in each state.

### Example (for `d=3`):

| State     | Value (`V`) | Policy (`π`) |
|-----------|-------------|--------------|
| `1`       | `3.66`      | Roll         |
| `2`       | `3.33`      | Roll         |
| `3`       | `3.00`      | Stop         |
| `1-2`     | `3.00`      | Stop         |
| `1-3`     | `4.00`      | Stop         |
| `2-3`     | `5.00`      | Stop         |
| `L`       | `0.00`      | -            |

---

## How to Run

1. **Run the Solver**:
   Customize the number of dice faces (`d`) in `main.py`.
   Execute `main.py` to calculate the optimal policy and value function.

   ```bash
   python main.py
   ```

3. **View Results**:
   - Value Matrix (`V`): Optimal value for each state.
   - Policy Matrix (`π`): Optimal action for each state.

---

## Observations

1. **Small `d`**:
   - Optimal policies are easier to compute and often involve stopping early to avoid risk.

2. **Larger `d`**:
   - More complex state space; optimal policies balance the trade-off between potential rewards and risk.

---

## About the Author

This implementation is part of my coursework in the Master MOSIG program at **Grenoble INP - ENSIMAG**, where I specialize in **Data Science and Artificial Intelligence (DSAI)**.

---

## License

This project is released under the [MIT License](LICENSE).
