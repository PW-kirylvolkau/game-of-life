# Usage

### CLI

Three scripts were created for user interaction:

```main.py```
Used for training models. The file requires the user to manually change the values of variables in the script itself (rather via CLI) - as the file was largely used for development purposes. This script also saves the trained models, for later usage.

```evaluate.py```

This file is the primary CLI for using the predictions. It will load a predifined (array in the script) iterative model and display the user with information about the trained models. Then the user may specify a .csv file containtng a board to run the prediction on, and save the prediction to another .csv file. The example (and the default option for this script) is in ./board.csv

### Directory structure

```./cone_models``` Contains definitions of submodels of the iterative model.
```./data``` Directory used for data
```./data_prep``` Contains functions necessary for parsing, formulating and restructuring data, to be fed to the model.
```./saved_models``` Default directory for saving trained models.
```./simulation``` Directory for functions related to Game of Life evolution
```./test_results``` Directory with notes from various tests (may be incomplete)

Files in the main directory are generally helper scripts for user interface functions, with the exception of ```predict.py```

```predict.py``` Contains functions used for using the models to predict cell states.
