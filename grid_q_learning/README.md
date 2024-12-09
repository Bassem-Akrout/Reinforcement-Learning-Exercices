
# Grid Robot Navigation - Reinforcement Learning

This repository contains an implementation of a grid-based Markov Decision Process (MDP) problem. The goal is to determine the optimal policy for maximizing the total reward in a grid environment, given specific rules and constraints.

---

## Problem Statement

### Environment Rules:
1. The grid contains:
   - **White cells**: The robot can move in any of the four directions (up, down, left, right).
       - Movement costs `0`.
       - Attempting to move out of bounds results in staying in place with a penalty of `-1`.
   - **Gray cells**: The robot automatically moves to a specific destination as indicated by an arrow.
       - Rewards are assigned based on the destination.
2. The robot's objective is to maximize the total reward with a **discount factor** $\gamma$.

### Tasks Implemented:
1. **Random Policy Evaluation**:
   - Compute the value of a random policy where the robot moves in any direction with equal probability (1/4).

2. **Value Iteration**:
   - Compute the optimal policy using value iteration with $\gamma = 0.9$.

---

## Implementation Details

### Structure

```
grid_q_learning/
├── input.py                   # Generates the input grid configuration (states, actions, transitions).
├── main.py                    # Main script to compute policies and values.
├── randompolicy.py            # Computes the value function for the random policy.
├── grid_game_input.json       # Input file for the grid configuration.
├── grid_game_random_policy.json # Output file with the random policy evaluation.
├── mdp_input.json             # Generated MDP input file for testing.
└── __pycache__/               # Cached Python files.
```

### Key Algorithms Implemented:
1. **Random Policy Evaluation**:
   - Calculates the expected value of each state under a random policy.
   - Probability of moving in any direction is \( rac{1}{4} \).

2. **Value Iteration**:
   - Iteratively updates the value function for each state until convergence.
   - Computes the optimal policy by selecting the action that maximizes the expected reward.

---

## How to Run

1. **Generate Input**:
   - The grid configuration and transitions are defined in `input.py`.
   - Run this script to generate `grid_game_input.json`.

   ```bash
   python input.py
   ```

2. **Random Policy Evaluation**:
   - Execute `randompolicy.py` to evaluate the value of the random policy.

   ```bash
   python randompolicy.py
   ```

   - Results are saved in `grid_game_random_policy.json`.

3. **Optimal Policy with Value Iteration**:
   - Run `main.py` to compute the optimal policy using value iteration.

   ```bash
   python main.py
   ```

---

## Observations

1. **Random Policy**:
   - The value of states depends on the uniform probability distribution over all possible actions.
   - Rewards are discounted by $\gamma$ at each step, resulting in lower values for distant states.

2. **Optimal Policy (Value Iteration)**:
   - The computed policy directs the robot toward the states with the highest cumulative rewards.
   - Convergence is achieved faster with a discount factor close to \(0.9\).

---

## Future Work

1. Implement Q-learning to compute the optimal policy and analyze the number of iterations required.
2. Compare the performance of Q-learning with value iteration.

---

## About the Author

This implementation is part of my coursework in the Master MOSIG program at **Grenoble INP - ENSIMAG**, where I specialize in **Data Science and Artificial Intelligence (DSAI)**.

---

## License

This project is released under the [MIT License](LICENSE).
