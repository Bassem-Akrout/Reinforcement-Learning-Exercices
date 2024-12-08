
# Exercise 1: Stochastic Shortest Path

This directory contains the implementation for **Exercise 1** in the series of Reinforcement Learning and Markov Decision Process (MDP) exercises. The goal of this exercise is to solve a stochastic shortest path problem by determining the deterministic policy that minimizes the expected cost to reach a terminal state.

---

## Problem Overview

In this exercise, we are tasked with solving a shortest path problem in a graph where transitions between states are stochastic. Given a Markov Decision Process (MDP) defined by:
- **States**: Represented as nodes in the graph.
- **Actions**: Choices available at each state.
- **Transitions**: Probabilistic outcomes of taking an action, with associated costs.

The objective is to compute:
1. The **value function** $V^*(s)$, which represents the minimum expected cost to reach the terminal state $P$ from any state $s$.
2. The **optimal policy** $ \pi^*(s) $, which specifies the best action to take in each state to achieve the minimum cost.

---

## Theoretical Insights

### Optimal Value Functions

1. **State Value Function $V^*(s)$**:
   $$
   V^*(s) = \min_a \sum_{s'} p(s' \mid s, a) \left[ c(s, a, s') + V^*(s') \right]
   $$
   - $p(s' \mid s, a)$: Probability of transitioning to state $s'$ from $s$ using action $a$.
   - $c(s, a, s')$: Cost of the transition.

2. **State-Action Value Function $Q^*(s, a)$**:
   $$
   Q^*(s, a) = \sum_{s'} p(s' \mid s, a) \left[ c(s, a, s') + V^*(s') \right]
   $$
   - $V^*(s) = \\min_a Q^*(s, a)$.

### Convergence
The Bellman updates iteratively refine the value function $V(s)$. The iterative updates rely on the contraction property of the Bellman operator, ensuring convergence to $V^*(s)$ for all states.

---

## Code Structure

```
Stochastic_Shortest_Path/
├── graph/
│   ├── __init__.py         # Graph module initialization
│   ├── node.py             # Contains the Node class
│   ├── action.py           # Contains the Action and Transition classes
│   └── graph.py            # Contains the Graph class
├── solver/
│   ├── __init__.py         # Solver module initialization
│   └── bellman_solver.py   # Contains the BellmanSolver class
├── graph.json              # Input JSON defining the problem
├── main.py                 # Entry point for solving the exercise
└── README.md               # This file
```

---

## How to Run

1. **Prepare Input JSON**: Define the graph structure and transition probabilities in `graph.json`. For example:
    ```json
    {
        "states_to_actions": {
            "A": ["B", "C"],
            "B": ["D", "E"]
        },
        "actions_to_resulting_states": {
            "B": {
                "D": [0.5, 2],
                "E": [0.5, 4]
            }
        }
    }
    ```

2. **Run the Solver**: Execute the `main.py` script:
    ```bash
    python main.py
    ```

3. **View the Output**:
    - **Value Matrix $V(s)$**: Minimum expected costs for each state.
    - **Policy Matrix $ \pi(s) $**: Optimal action for each state.

---

## Example Results

For the provided input graph:
- **Value Matrix $V(s)$**:
    ```
    A: 10.0
    B: 8.0
    D: 5.0
    ```

- **Policy Matrix $ \pi(s) $**:
    ```
    A: B
    B: D
    ```

---

## Notes

This exercise is part of a series of exercises on Reinforcement Learning and MDPs. Refer to the [main README](../README.md) for an overview of the series.

---

## License

This project is released under the [MIT License](../LICENSE).
