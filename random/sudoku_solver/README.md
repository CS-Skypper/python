# sudoku solver 
## using Backtracking Algorithm

### Aproaching the problem:
1. Pick an empty square
2. Try all numbers
3. Find one that fits
4. Move on

Giving a board in a 2D array form


### Difference between **Naif** Algorithm and **Backtracking** Algorithm?
  - When getting to a point where the solution cannot be completed we _backtrack_
    - _"completing a square at a time and just keep recursively checking to make sure all these solutions work until we eventually reach one that does work"_
  - Rather than trying to continue a solution that can never possibly work, which the Naive Algorithm does, Backtracking will only continue solutions that currently work and if they don't work will backtrack to the last step and try something again.
  - Trying any possible combination will generate a 9 to 81 different solutions and try them all on the board until finds one that work. Not really efficient.