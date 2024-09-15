# Branch and Bound

## Notes

- Optimization problem is a problem that demand either minimum result or maximum result.
- Branch and bound is used for solving optimization problems (NOTE: for solving only minimization problems not maximization problems).
- Possible Solutions --> Feasible Solutions --> Optimal Solution.
- Brute force approach says that for any given problem, we should try out all possible solutions and pick up desired solutions.
- Branch and bound uses brute force approach.

## Difference between backtracking and branch & bound

- Backtracking follows DFS while generating state-space tree.
- Branch and bound follows BFS while generating state-space tree.

## FIFO branch and bound vs LIFO branch and bound

- FIFO branch and bound: uses queue for next node exploration in BFS.
- LIFO branch and bound: uses stack for next node exploration in BFS.
- LC (Least Cost) branch and bound: only explore the node with least cost among all nodes in a given level in BFS.
