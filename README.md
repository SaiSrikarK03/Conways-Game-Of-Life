# Conways-Game-Of-Life
This Python script simulates Conway's Game of Life using Pygame. It features a dynamic grid that adjusts to window resizing, allows users to paint cells alive or dead, and toggles the simulation with the spacebar. A simple UI displays the game's paused or running state, with a toggle option for visibility.
A Python implementation of Conway's Game of Life using Pygame. This project allows users to interactively create and simulate the evolution of cellular automata based on Conway's rules.

## Description
Conway's Game of Life is a zero-player game, meaning its evolution is determined by its initial state, requiring no further input. Players can create an initial configuration and observe how it evolves according to the following rules:
1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

This implementation features a dynamic grid displayed in a window, allowing users to toggle cells between alive (white) and dead (black) states by clicking on them. The simulation can be paused and resumed using the spacebar, and a simple UI displays the current state of the game.

## Features
- Interactive grid where users can click to toggle cell states.
- Spacebar to pause/resume the game.
- UI to indicate if the game is paused or running.
- Toggle the visibility of the pause/resume UI using the 'H' key.

## Installation

To run this project, you will need Python and Pygame installed on your system. You can install Pygame using pip:

```bash
pip install pygame
```

## Usage
1. Clone this repository:

   ```bash
   git clone https://github.com/SaiSrikarK03/Conways-Game-Of-Life.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Conways-Game-Of-Life
   ```

3. Run the script:

   ```bash
   python ConwaysGameOfLife/ConwaysGameOfLife.py
   ```

4. Instructions:
   - **Left-click** on the grid to set a cell to alive (white).
   - **Right-click** to set a cell to dead (black).
   - Press the **spacebar** to start or pause the simulation.
   - Press **H** to toggle the pause/resume status UI.

Enjoy!!!
