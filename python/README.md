# Conway's Game of Life Implementation Manual

## Data format

Functions available in ```generate.py``` file are used for creating and porting the data either to the GUI or the Game of Life actor and model. Therefore for portability the format in which boards are stored is as follows:
If the board size is ```n``` then the output format will be a binary array of length ```n^2```. The ```i-th``` position in the array corresponds to ```floor(i / n)``` row and ```i mod n``` column.

Simulation logic is available in ```gameoflife.py```, where the function ```step()``` performs one step of the Game of Life. The function takes as input a square matrix of a specified size and returns a matrix of the same size, containing the next iteration of the Game of Life.

## Testing status

Functions in ```gameoflife.py``` need to be tested.

