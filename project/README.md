# Transaction Analyzer Project
#### Video Demo:  <https://youtu.be/Smzy-cITASk>
#### Description:
This project is a simple Personal Finance Tracker implemented in Python. It allows users to add, view, and analyze their income and expenses.
The main features of the project include adding new transactions, displaying all transactions, and analyzing the total income and expenses.


### Files:
- `project.py`: Contains the main logic of the application including functions to add transactions, show transactions, and analyze transactions.
- `test_project.py`: Contains test functions for each custom function in project.py. These tests ensure that the functions behave as expected.
- `transactions.csv`: An example CSV file containing sample transaction data used by the application.
- `requirements.txt`: Lists the dependencies required to run the project, primarily pytest for testing.

### Functions:
1. **main**: The entry point of the application which provides a menu interface for users to add transactions, view transactions, analyze transactions, or exit the program.
2. **add_transaction**: Prompts the user to enter the details of a transaction including the date, category, amount, and description. It validates the date format and ensures the amount is stored as a formatted float. It then creates a Transaction object for CSV file.
3. **save_transaction**: Saves the provided Transaction object to a CSV file. It handles potential errors related to file operations.
4. **show_transactions**: Reads and displays all the transactions stored in the CSV file. It handles potential errors related to file operations.
5. **analyze_transactions**: Reads the transactions from the CSV file and calculates the total income and total expense. It prints out the results and handles potential errors related to file operations and data conversion.

### Design Choices:
-The application reads and writes data to a CSV file using the built-in csv module, ensuring compatibility and ease of use.
-The application validates the date format using regular expressions to ensure correct input.
-The total income and expense are calculated to provide insights into financial data.
-The design is user-friendly, providing a simple menu interface for interaction.

### Testing:
The project includes a suite of tests using pytest. Each custom function has corresponding test functions to validate their correctness. The tests ensure that:

-Transactions are added correctly to the CSV file.
-Transactions are displayed accurately.
-The total income and total expense are calculated correctly.

### How to Run:
1. Ensure that Python and pytest are installed on your system.
2. Clone the project repository or download the project files.
3. Navigate to the project directory.
4. Run the main application using python project.py.
5. Run the tests using pytest test_project.py.

This project demonstrates the use of file I/O, regular expressions, exception handling, and object-oriented programming concepts in Python.
It showcases practical applications of these concepts in real-world scenarios such as financial data analysis.






