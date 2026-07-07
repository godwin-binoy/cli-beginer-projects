# Ram Filler

Ram Filler is a Python program designed to intentionally fill the system's RAM until it crashes. It serves as a demonstration of how resource-intensive loops can impact a system's performance. This tool should only be used for educational or experimental purposes on systems where you can safely handle a crash.



## How It Works

The script continuously doubles the size of a string in an infinite loop. This rapidly consumes the system's memory, ultimately leading to a crash.

### Code Explanation:
1. **Introduction**:
   - The program introduces itself via a print statement.
   ```python
   print('Ram Filler\n----------\n\nThis program will crash automatically after filling ram\n')
   ```

2. **User Input**:
   - It prompts the user to press Enter to start.
   ```python
   input('Enter to fill ram : ')
   ```

3. **Infinite Loop**:
   - A string variable `data` is continuously doubled, causing memory consumption to grow exponentially.
   ```python
   data = '0'
   print('Filling ram...')
   while True:
       data += data
   ```

## Requirements

- Python 3

## Usage Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/godwin-binoy/Ram-filler.git
   ```
2. Navigate to the directory:
   ```bash
   cd Ram-filler
   ```
3. Run the script (use caution):
   ```bash
   python3 "Ram filler.py"
   ```

   > **Note:** Save all work and close unnecessary programs before running the script.



## Use Cases

- **Educational Purposes**: Learn how memory usage works and the impact of infinite loops.
- **System Testing**: Test how well a system handles memory overloads (e.g., for debugging or stress testing).



## Best Practices

1. Run this program only in a controlled environment, such as a virtual machine or test system.
2. Ensure no critical work is open on the system.
3. Monitor system resources while running the script to observe its behavior.



## Contributing

Contributions are welcome! If you have ideas to improve this project or add additional features, feel free to fork the repository and submit a pull request.

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.



## Acknowledgements

- Inspired by the need to understand memory consumption behavior in programming.



## ⚠️ Disclaimer

This program is designed to crash the system by consuming all available RAM. Use it **at your own risk**. Only run it on systems where a crash will not result in data loss or other consequences. The creator of this repository is not responsible for any damage caused by the misuse of this program.

## Warning

This program is highly destructive by design. Do not use it on production systems or devices with critical data.

## Author 

https://github.com/godwin-binoy

---
