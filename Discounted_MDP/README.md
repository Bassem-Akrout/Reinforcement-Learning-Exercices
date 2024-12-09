
# Example of a Discounted MDP

> **Update**: An issue in the Bellman solver implementation caused errors when $\gamma = 1$ or $p = 1$, leading to unintended behaviors. This issue has been resolved, ensuring the algorithm works correctly across all configurations.

This repository contains an implementation of a discounted Markov Decision Process (MDP). The goal is to explore the impact of parameters like the discount factor ($\gamma$) and transition probabilities ($p$) on the resulting policies and value functions.

---

## Problem Statement

Consider an MDP with:
- **State space**: $\{0, 1, \dots, 10\}$
- **Action space**: $\{A, B\}$

### Actions and Transitions
- **Action A**: 
  - Moves the agent to state $0$ with probability $1$.
  - Provides an immediate reward equal to the current state $s$.
- **Action B**:
  - Moves the agent to state $(s+1) \mod 10$ with probability $p$.
  - Moves the agent to state $0$ with probability $1-p$.
  - Provides an immediate reward of $0$.

### Objective
Find and evaluate policies that maximize the expected **discounted reward** for a given discount factor $\gamma$ ($0 \leq \gamma \leq 1$).

---

## Key Observations

1. **Impact of $\gamma$:**
   - When $\gamma = 1$: 
     - Rewards from future states are not attenuated, but the algorithm might fail to converge due to infinite value propagation.
   - When $\gamma < 1$: 
     - The algorithm converges properly, balancing immediate and future rewards.

2. **Impact of $p$:**
   - Higher $p$: The policy is more inclined to choose **B** to pursue higher rewards in future states.
   - Lower $p$: The policy tends to favor **A**, ensuring immediate rewards.

3. **Threshold Behavior:**
   - A critical threshold exists for $\gamma \cdot p$, where the policy shifts from favoring **A** to favoring **B**.

---

## Implementation Details

### Structure

```
Discounted_MDP/
├── input.py                   # Generates input MDP data based on reward functions and transition probabilities.
├── main.py                    # Main script to solve the MDP and visualize results.
├── solver/ 
│   ├── bellman_solver.py      # Implements the Bellman equation for value iteration.
│   └── __init__.py 
├── mdp_input.json             # Example input file for the MDP.
├── gamma_0,9.png              # Plot for policy behavior at $\gamma = 0.9$.
├── gamma_1.png                # Plot for policy behavior at $\gamma = 1$.
└── plot_policy_transitions.py # generates a plot showing how policy decisions change as the probability 
𝑝
p varies
```

### Reward Functions

The script supports various reward functions to test different behaviors:
- **Linear**: $r(s) = s$
- **Quadratic**: $r(s) = s^2$
- **Cubic**: $r(s) = s^3$
- **Exponential**: $r(s) = \exp(s)$

### Results

- The policy and value functions are calculated using **value iteration**.
- Plots (e.g., `gamma_0,9.png`) illustrate the policy decisions across different states and probabilities.

---

## How to Run

1. **Generate Input**: Customize parameters in `input.py`.
2. **Run the Solver**: Execute `main.py` to calculate the optimal policy.
3. **Visualize Results**: View plots of policy changes (e.g., as $p$ or $\gamma$ varies).

```bash
python main.py
```

---

## Observations for Specific Configurations

1. **$\gamma = 1$ and $p = 1$:**
   - Policies favor immediate rewards ($A$) for all states, as the algorithm fails to fully account for long-term gains.
2. **$\gamma = 0.9$ and $p = 0.4-0.5$:**
   - The policy transitions from **A** to **B** for most states, reflecting a balanced trade-off between immediate and future rewards.

---

## About the Author

This implementation is part of my coursework in the Master MOSIG program at **Grenoble INP - ENSIMAG**, where I specialize in **Data Science and Artificial Intelligence (DSAI)**.

---

## License

This project is released under the [MIT License](LICENSE).
