# Backtracking

## Notes

- Brute force approach says that for any given problem, we should try out all possible solutions and pick up desired solutions.
- Backtracking uses brute force approach.
- Backtracking is used when a problem has multiple solutions and you want all those solutions.
- state-space tree: A state-space tree is a conceptual representation used in backtracking algorithms to explore all possible states or solutions of a problem systematically. It helps in visualizing the sequence of decisions made during the process and aids in understanding how the algorithm progresses and prunes suboptimal or invalid solutions.
- bounding function: A bounding function (condition) in backtracking is a critical tool used to prune branches of the state-space tree that are guaranteed not to lead to valid or optimal solutions. The function determines whether further exploration of a particular node (or state) is necessary, saving computational time by avoiding unnecessary exploration of subtrees.

## Difference between backtracking and branch & bound

- Backtracking follows DFS while generating state-space tree.
- Branch and bound follows BFS while generating state-space tree.
