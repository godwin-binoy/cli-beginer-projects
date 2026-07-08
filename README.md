# CLI Projects Collection

A consolidated repository of command-line tools, mini-games, and system utilities. This workspace contains a variety of beginner-friendly scripts demonstrating core programming logic, loop control, user input validation, and memory allocation across Python, Java, and C.

---

## Repository Structure

```text
cli-beginer-projects/
├── Character-Counter/
│   └── Character-counter.py
├── Dice/
│   └── Dice.py
├── Guss-The-Number/
│   └── Guss The Number.py
├── Math-Game/
│   └── Math-Game.py
├── Multiplication-Table/
│   ├── multiplication_table.c
│   ├── multiplication_table.java
│   └── Multiplication-table.py
├── Password-Generator/
│   └── Pasword generator.py
├── Ram-filler/
│   └── Ram filler.py
└── Random-number-generator/
    └── random number generator.py
```

---

## Project Index

The table below lists each project, the programming languages used, and their respective directories.

| Project Name | Language | Directory | Description |
| :--- | :--- | :--- | :--- |
| Multiplication Table | C, Java, Python | `Multiplication-Table/` | Generates products (1 to 10) for any input number. |
| Character Counter | Python | `Character-Counter/` | Counts and displays the length of a user-entered string. |
| Dice Simulator | Python | `Dice/` | Simulates a standard 6-sided dice roll. |
| Guess The Number | Python | `Guss-The-Number/` | A game where you guess a hidden number within a dynamic range. |
| Math Game | Python | `Math-Game/` | Interactive arithmetic test with difficulty scaling and scoring. |
| Password Generator | Python | `Password-Generator/` | Dynamically builds secure random passwords. |
| RAM Filler | Python | `Ram-filler/` | Stress-tests local memory by continuously duplicating data. |
| Random Number Generator | Python | `Random-number-generator/` | Generates a single random integer within user-defined bounds. |

---

## Detailed Project Overviews

### 1. Multiplication Table
This utility displays multiplication tables for any valid integer. It is implemented in three programming languages to showcase syntax parity, looping structures, and basic input validation across Python, Java, and C.
* **Key Concepts:** Type parsing, exception handling, and input sanitization.
* **How to Run:**
  * **Python:**
    ```bash
    python Multiplication-Table/Multiplication-table.py
    ```
  * **C (Compile and Run):**
    ```bash
    gcc Multiplication-Table/multiplication_table.c -o multiplication_table
    ./multiplication_table
    ```
  * **Java (Compile and Run):**
    ```bash
    javac Multiplication-Table/multiplication_table.java
    java -cp Multiplication-Table multiplication_table
    ```

### 2. Character Counter
Analyzes text provided by the user in the command line and outputs the total length of the string.
* **Key Concepts:** Standard input operations and basic string attributes.
* **How to Run:**
  ```bash
  python Character-Counter/Character-counter.py
  ```

### 3. Dice Simulator
Simulates a physical dice roll, producing a random integer between 1 and 6 each time the user presses enter.
* **Key Concepts:** Standard randomization libraries and execution loop controls.
* **How to Run:**
  ```bash
  python Dice/Dice.py
  ```

### 4. Guess The Number
Calculates dynamic guessing attempts using logarithmic math based on user-provided boundaries, and guides the player to find the target number with high-or-low feedback.
* **Key Concepts:** Logarithmic calculations, conditional branches, and user input validation.
* **How to Run:**
  ```bash
  python "Guss-The-Number/Guss The Number.py"
  ```

### 5. Math Game
An arithmetic quiz generator where users answer random problems based on their chosen level (numbers from 1 to 10, 100, or 1000). Points are earned for correct answers, and the score resets on a loss.
* **Key Concepts:** Arithmetic logic, game state resetting, and error-handling fallback functions.
* **How to Run:**
  ```bash
  python Math-Game/Math-Game.py
  ```

### 6. Password Generator
Builds random passwords of specified lengths. Users can toggle the inclusion of uppercase characters, lowercase characters, numbers, and symbols.
* **Key Concepts:** Set containment, sampling libraries, and character mapping arrays.
* **How to Run:**
  ```bash
  python "Password-Generator/Pasword generator.py"
  ```

### 7. RAM Filler
Duplicates an initialized variable exponentially inside an infinite loop to demonstrate operating system behavior and limitations during rapid RAM consumption.
* **Key Concepts:** Loop constructs and memory consumption limitations.
* **How to Run:**
  ```bash
  python "Ram-filler/Ram filler.py"
  ```

### 8. Random Number Generator
Outputs a single randomized integer value based on the lowest and highest number limits configured by the user.
* **Key Concepts:** Parsing command inputs, mathematical boundaries, and random sampling.
* **How to Run:**
  ```bash
  python "Random-number-generator/random number generator.py"
  ```

---

## Getting Started

### Prerequisites
Running these scripts locally requires the installation of the appropriate development toolkits or runtimes:
* **Python 3.x**
* **GCC Compiler** (for running the C script)
* **Java Development Kit (JDK)** (for running the Java class)

### Installation
1. Clone this repository to your system:
   ```bash
   git clone https://github.com/godwin-binoy/cli-beginer-projects.git
   ```
2. Change into the root directory:
   ```bash
   cd cli-beginer-projects
   ```
3. Use the commands described in the [Detailed Project Overviews](#detailed-project-overviews) section to run your desired script.

---

## Contributing
If you find areas of improvement, or wish to contribute additional tools to this collection:
1. Fork the repository.
2. Create a clean feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Describe your contribution briefly"
   ```
4. Push your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a Pull Request for review.

---

## License
This project is open-source and available under the MIT License. Feel free to use, modify, and reference the code for educational purposes.
