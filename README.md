# FLA_ProjectDemo_DFASubstringValidator
Objective
The objective of this project is to create a Deterministic Finite Automaton (DFA) simulator with a graphical user interface (GUI) to check whether a given input string meets certain conditions:

Contains the substring "abc".
Has an even length.
Has an odd length.
This project helps visualize and understand the concept of DFAs and their application in language recognition.

Software Used
Python: For implementing the DFA logic and functionality.
Tkinter: To build the GUI, allowing easy user interaction.
Visual Studio Code (VS Code): Used as the code editor for writing, debugging, and testing the Python code.
Libraries
Python: A high-level programming language used for the core logic of the DFA.
Tkinter: A built-in Python library that provides tools for creating GUI applications. It’s used here to:
Design the GUI window for user input.
Add buttons for selecting DFA checks.
Display the results of each DFA simulation.
Project Structure
The project consists of the following classes:

State:
Represents a single state in the DFA, including its name, whether it’s an accepting state, and the transitions to other states.

DFA:
Defines the DFA structure, with methods to add states, set the start state, add transitions, and simulate whether an input string is accepted.

DFAFactory:
Provides specific DFA configurations:

contains_substring_abc: Checks if the input string contains the substring "abc".
even_length: Checks if the input string has an even length.
odd_length: Checks if the input string has an odd length.
DFASimulatorApp:
Builds the GUI using Tkinter. Allows users to input strings, select DFA checks, and see results based on whether the input string meets the DFA conditions.

How to Run the Project
Prerequisites:

Ensure Python is installed on your system.
Tkinter is included with Python, so no additional installation is required.
Steps:

Clone or download this repository.
Open the project in Visual Studio Code (or your preferred Python editor).
Run the main Python file using:
bash
Copy code
python <filename>.py
A GUI window will appear where you can input a string, select the check type, and view the results.
Usage
Enter a string of characters (allowed characters are 0, 1, a, b, and c).
Click on the appropriate button to check:
"Contains 'abc'": Checks if the input string contains "abc".
"Even Length": Checks if the input string has an even number of characters.
"Odd Length": Checks if the input string has an odd number of characters.
The result will display either "Accepted!" or "Rejected!" based on whether the string meets the selected condition.
Example
Input: abc0

Check: Contains "abc"
Result: Accepted!
Input: 1010

Check: Even Length
Result: Accepted!
Input: 1001

Check: Odd Length
Result: Accepted!
Future Enhancements
Add more DFA configurations for additional checks.
Improve the GUI design for a more user-friendly experience.
License
This project is open-source and free to use.
