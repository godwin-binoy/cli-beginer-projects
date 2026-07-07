# Password Generator

A Python-based command-line tool for generating secure passwords. The tool allows users to customize their passwords by including or excluding numerals, capital letters, small letters, and symbols.

## Features

- Generate passwords of custom lengths.
- Option to include or exclude:
  - Numerals
  - Capital letters
  - Small letters
  - Symbols
- User-friendly prompts and error handling.

## Prerequisites

- Python 3 installed on your system.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/godwin-binoy/Password-Generator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Password-Generator
   ```

3. Ensure Python is installed by running:

   ```bash
   python --version
   ```

## Usage

1. Run the script:

   ```bash
   python3 password_generator.py
   ```

2. Follow the on-screen prompts:

   - Input whether to include numerals (y/n).
   - Input whether to include capital letters (y/n).
   - Input whether to include small letters (y/n).
   - Input whether to include symbols (y/n).
   - Specify the desired password length (must be a numerical value).

3. The generated password will be displayed on the screen.

4. To generate another password, press Enter. To exit, type `exit`.

### Example Workflow

1. Start the script:
   ```
   Password Generator
   ------------------
   Length: 12
   'y' = yes
   'n' = no
   ---------
   Include Numericals in password?
   Enter here: y
   Include Capital letters in password?
   Enter here: y
   Include Small letters in password?
   Enter here: y
   Include Symbols in password?
   Enter here: y
   Password: A1b@c2d#E3
   ```

## Code Explanation

### Libraries Used

- `random`: To randomly shuffle and sample characters for the password.

### Main Functions

#### `ask_user()`

This function prompts the user to choose whether to include numerals, capital letters, small letters, and symbols in their password. Based on the user's input, it constructs a string of allowed characters.

#### Password Length

The user specifies the password length. If the input is invalid (not a number), an error message is displayed, and the input is re-requested.

#### Password Generation

Using the `random.sample()` method, the script generates a random password by selecting characters from the user-defined pool of allowed characters.

### Error Handling

- If no character types are selected, the script prompts the user again.
- If the desired password length exceeds the number of available characters, an error message is displayed.

## Customization

- To add or modify the character pool (e.g., include additional symbols), edit the variables in the script:
  ```python
  numbers = '1234567890'
  capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  small_letters = 'abcdefghijklmnopqrstuvwxyz'
  symbols = '@#_&-+()/*:;!?.~`\''"|=\u00b0<>{}\%[]'
  ```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contribution

Feel free to fork the repository and submit pull requests for improvements or additional features.

## Contact

For questions or suggestions, please reach out to the repository owner through GitHub.



## Author :

[https://github.com/godwin-binoy](https://github.com/godwin-binoy)

---
