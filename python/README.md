# Conway's Game of Life Implementation Manual

## Data format

Functions available in ```generate.py``` file are used for creating and porting the data either to the GUI or the Game of Life actor and model. Therefore for portability the format in which boards are stored is as follows:
If the board size is ```n``` then the output format will be a binary array of length ```n<sup>2</sup>```. The ```i-th``` position in the array corresponds to ```floor(i / n)``` row and ```i mod n``` column.

## Testing status

At the moment all functions have been tested.

## TODO

    [  ] Implement the Game of Life simulator

