# Single-Player Infexion
This project was created as part of an artificial intelligence subject in a team of 2, and required finding the shortest sequence of moves, given an Infexion board state (game rules described [here](https://github.com/tristankthomas/two-player-infexion)), in order for the red player to win (take control of all blues tokens). This was achieved using the A* graph search algorithm using an admissible heuristic defined in `heuristic.py`. 
## Usage
The program can be executed by running the `search` module and passing in a test csv file through stdin for example:
```
python -m search < test.csv
```
The csv files are formatted with each row represented either a red or blue cell with the first two elements being the coordinates, followed by the colour and then the power. A test creation script was created to create a custom board configuration and the option to pass this test without stdin is commented out in `__main__.py`.
