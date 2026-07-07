# Guess The Number

## Overview

**Guess The Number** is a Python-based terminal game where players guess a randomly generated number within a specified range. The game provides a set number of chances to the player, determined by the range of numbers, and offers feedback on whether the guessed number is too high or too low. The game is designed to be simple, interactive, and fun for users of all ages.



## Features

- **Custom Range:** Players can input their desired lower and upper bounds for the number range.
- **Dynamic Difficulty:** The number of chances is calculated based on the range size using logarithmic scaling.
- **User-Friendly Feedback:** The game provides hints after each guess, indicating whether the target number is smaller or larger.
- **Reset Options:** Players can reset the range or replay the game without restarting the program.
- **Exit Anytime:** Players can exit the game by typing `exit`.



## Installation

### Prerequisites

Ensure you have Python installed on your system. The script is compatible with Python 3

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/godwin-binoy/Guss-The-Number.git
   ```
2. Navigate to the directory:
   ```bash
   cd Guss-The-Number
   ```
3. Run the script:
   ```bash
   python3 "Guss The Number.py"
   ```



## How to Play

1. Run the script using the terminal.
2. Enter the lower and upper bounds of the number range when prompted.
3. The game will calculate the number of chances based on the range.
4. Guess the number within the given chances:
   - If your guess is too high, the game will indicate "It's smaller than you guessed."
   - If your guess is too low, the game will indicate "It's larger than you guessed."
   - If you guess correctly, the game will display "It's the number. You done it!"
5. After each round:
   - Type `exit` to quit the game.
   - Type `reset` to enter a new range.
   - Press `Enter` to play again with the same range.



## Example Gameplay

```
Guss The Number
---------------

Enter Lower range of number

  : 1

Enter Higher range of number

  : 100

You have 7 Chances

Guss the number : 50

It's larger than you guessed
You have 6 more chances

Guss the number : 75

It's smaller than you guessed
You have 5 more chances

Guss the number : 63

It's the number
You done it !

Enter 'exit' to exit
Enter 'reset' to reset the range
Press enter to play again :
```



## Code Explanation

The script uses:

- **Random Number Generation:**

  ```python
  random.randint(lower_range, higher_range)
  ```

  To generate a random number within the specified range.

- **Logarithmic Calculation:**

  ```python
  player_chances = round(math.log(higher_range + lower_range + 1, 2))
  ```

  To determine the number of chances, making the game challenging yet fair.

- **Input Validation:**
  The game ensures that inputs for range and guesses are integers, prompting errors otherwise.



## Contribution

Contributions are welcome! Feel free to submit a pull request or open an issue on GitHub.



## License

This project is licensed under the [MIT License](LICENSE).


## Contact

For any inquiries or feedback, reach out to the repository owner at [GitHub Profile](https://github.com/godwin-binoy).

## Author 

https://github.com/godwin-binoy

---
