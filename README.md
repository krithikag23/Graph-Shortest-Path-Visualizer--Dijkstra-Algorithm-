# Dijkstra & A* Shortest Path Finder

This project computes and visualizes the shortest path in a weighted graph using:

- **Dijkstra Algorithm** (min-heap)
- **A\*** Algorithm (heuristic search)

It also provides visual graph output highlighting the shortest path.

---

## Features
- Calculates shortest path between any two nodes
- Supports both Dijkstra and A* algorithms
- JSON-based graph input
- Path reconstruction for both algorithms
- Visual graph rendering using:
  - Node labels
  - Edge weights
  - Highlighted path (green for Dijkstra, red for A*)
- Comparison visualization: Dijkstra vs A*


---
## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

## Benchmark: Dijkstra vs A*
The project includes benchmarking to compare:
- Number of nodes visited
- Execution time

A* typically explores fewer nodes due to heuristic guidance,
making it more efficient on large graphs and map-based problems.

## Grid-Based Pathfinding (Game Style)

This project also includes **2D grid-based pathfinding** using the A* algorithm,
similar to how pathfinding works in games and robotics.

### Features
- Grid cells:
  - `0` → free cell
  - `1` → obstacle
- A* algorithm with Manhattan heuristic
- Shortest path reconstruction
- Visual grid display with highlighted path
- **Diagonal movement (8-direction support)**

### Run Grid Pathfinding
```bash
python grid_main.py
```

## Animated Grid Pathfinding (A*)

The grid-based A* implementation includes a **step-by-step animation**
that visualizes how the algorithm explores the grid.


- Blue cells: explored nodes
- Green line: final shortest path
- Black cells: obstacles
- Supports diagonal movement for natural, game-like paths

### Run Grid Animation:
```bash
python grid_animate.py
```

## BFS vs A* Animated Comparison
The repository includes a side-by-side animated comparison of **BFS** and **A\*** on the same 2D grid.


### Comparison Highlights
- BFS explores the grid uniformly without a heuristic
- A* uses heuristic guidance to reach the goal faster
- A* typically visits fewer nodes than BFS

### Animation Legend
- Blue cells → explored nodes
- Green path → final shortest path
- Black cells → obstacles

### Run Comparison
```bash
python compare_bfs_astar.py
```
