# Dice

A simple Python-based dice rolling simulator.

## Overview

This project is a basic dice rolling simulator written in Python. It generates a random number between 1 and 6 to simulate the rolling of a six-sided die. Each time the user presses `Enter`, the dice rolls and displays the result.

## Features

- Simulates a six-sided die.
- Generates random results with each roll.
- Simple and intuitive command-line interface.

## Prerequisites

To run this script, ensure you have the following installed on your system:

- Python 3

You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/)

## How to Use

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/godwin-binoy/Dice.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Dice
   ```

3. Run the `Dice.py` script:

   ```bash
   python Dice.py
   ```

4. Press `Enter` to roll the dice. The result will be displayed in the console.

5. To exit the program, use `Ctrl+C` or close the terminal window.

## Code Explanation

The `Dice.py` script:

1. Imports the `random` module to generate random numbers.
2. Continuously prompts the user to press `Enter` to roll the dice.
3. Uses `random.randint(1, 6)` to generate a random integer between 1 and 6.
4. Displays the result in a simple ASCII representation.

### Sample Output

```
Dice
----

Enter to roll dice :

-----
| 3 |
-----

Enter to roll dice :

-----
| 6 |
-----
```

## Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request. Please ensure your changes are well-documented and tested.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

https://github.com/godwin-binoy 

---