*This project has been created as part of the 42 curriculum by nel-adao and mjabri.*

# A-Maze-ing

## Description
This project is a Python maze generator. It creates random mazes, visualizes them in the terminal with colors, and saves the result to a file. It can solve itself and ensures there is always a valid path from start to exit.

## Instructions
1.  **Install:** Run `make install` to set up dependencies.
2.  **Run:** Execute `make run` to generate and view the maze.
3.  **Clean:** Use `make clean` to remove temporary files.

## Configuration File
The `config.txt` file controls the maze generation. The format is `KEY = VALUE`.
* `WIDTH` / `HEIGHT`: Size of the maze.
* `ENTRY` / `EXIT`: Coordinates (e.g., `0,0`).
* `OUTPUT_FILE`: Where to save the hex map.
* `PERFECT`: `True` for a single path, `False` for loops.
* `ALGO`: `DFS` or `PRIM`.
* `SEED`: `True` to make the maze reproducible.

## Algorithms
We implemented two algorithms:
* **DFS (Depth-First Search):** We chose this because it's efficient and creates long, winding corridors, which makes the maze look complex and fun to solve.
* **Prim's Algorithm:** Creates a more natural, branching structure with fewer long corridors.

## Reusability
The core logic is separated into the `mazegen` package. You can import it in other Python projects like this:
```python
from mazegen import MazeGenerator, ft_get_config