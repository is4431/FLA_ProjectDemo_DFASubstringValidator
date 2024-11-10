import tkinter as tk

class State:
    def __init__(self, name, is_accept=False):
        self.name = name
        self.is_accept = is_accept
        self.transitions = {}

    def add_transition(self, symbol, state):
        self.transitions[symbol] = state  # Deterministic: One transition per symbol

class DFA:
    def __init__(self):
        self.states = {}
        self.start_state = None

    def add_state(self, name, is_accept=False):
        state = State(name, is_accept)
        self.states[name] = state
        return state

    def set_start(self, name):
        self.start_state = self.states[name]

    def add_transition(self, from_state, symbol, to_state):
        self.states[from_state].add_transition(symbol, self.states[to_state])

    def simulate(self, input_string):
        current_state = self.start_state
        
        for symbol in input_string:
            if symbol in current_state.transitions:
                current_state = current_state.transitions[symbol]
            else:
                return False  # If no valid transition, reject the input
        
        return current_state.is_accept

class DFAFactory:
    @staticmethod
    def contains_substring_abc():
        dfa = DFA()
        dfa.add_state("q0")  # Start state
        dfa.add_state("q1")  # State after 'a'
        dfa.add_state("q2")  # State after 'ab'
        dfa.add_state("q_accept", is_accept=True)  # Accept state after 'abc'
        dfa.set_start("q0")

        # Transitions for detecting "abc" anywhere in the string
        dfa.add_transition("q0", 'a', "q1")
        dfa.add_transition("q1", 'b', "q2")
        dfa.add_transition("q2", 'c', "q_accept")

        # Self-loop for characters in q0 to ignore anything before "a"
        for char in ['0', '1', 'b', 'c']:
            dfa.add_transition("q0", char, "q0")

        # Transition to stay in q1 if another 'a' comes before 'b'
        dfa.add_transition("q1", 'a', "q1")
        for char in ['0', '1', 'c']:
            dfa.add_transition("q1", char, "q0")  # Reset if sequence breaks

        # Transition to reset if sequence breaks in q2
        dfa.add_transition("q2", 'a', "q1")
        for char in ['0', '1', 'b']:
            dfa.add_transition("q2", char, "q0")  # Reset if sequence breaks

        # Accept state loops for any character
        for char in ['a', 'b', 'c', '0', '1']:
            dfa.add_transition("q_accept", char, "q_accept")

        return dfa


    @staticmethod
    def even_length():
        dfa = DFA()
        dfa.add_state("q0", is_accept=True)  # Start state (also accepting)
        dfa.add_state("q1")  # State for odd length
        dfa.set_start("q0")

        # Alternate between q0 and q1 for each character
        for char in ['0', '1', 'a', 'b', 'c']:
            dfa.add_transition("q0", char, "q1")  # Even to odd
            dfa.add_transition("q1", char, "q0")  # Odd to even

        return dfa

    @staticmethod
    def odd_length():
        dfa = DFA()
        dfa.add_state("q0")  # Start state
        dfa.add_state("q1", is_accept=True)  # Accept state for odd length
        dfa.set_start("q0")

        # Alternate between q0 and q1 for each character
        for char in ['0', '1', 'a', 'b', 'c']:
            dfa.add_transition("q0", char, "q1")  # Even to odd
            dfa.add_transition("q1", char, "q0")  # Odd to even

        return dfa

class DFASimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DFA Language Checker")

        # Input label and field
        self.input_label = tk.Label(root, text="Enter a binary string (or 'a', 'b', 'c'):")
        self.input_label.pack()

        self.input_field = tk.Entry(root)
        self.input_field.pack()
        self.input_field.focus_set()  # Automatically focus on input field

        # Create buttons for each condition
        self.check_button_substring = tk.Button(root, text="Check Contains 'abc'", command=self.check_contains_abc)
        self.check_button_substring.pack()

        self.check_button_even = tk.Button(root, text="Check Even Length", command=self.check_even_length)
        self.check_button_even.pack()

        self.check_button_odd = tk.Button(root, text="Check Odd Length", command=self.check_odd_length)
        self.check_button_odd.pack()

        # Result label
        self.result_label = tk.Label(root, text="Result: ")
        self.result_label.pack()

        # Initialize DFAs
        self.dfa_contains_abc = DFAFactory.contains_substring_abc()
        self.dfa_even_length = DFAFactory.even_length()
        self.dfa_odd_length = DFAFactory.odd_length()

    def check_contains_abc(self):
        self.check_language(self.dfa_contains_abc, "Contains 'abc'")

    def check_even_length(self):
        self.check_language(self.dfa_even_length, "Even Length")

    def check_odd_length(self):
        self.check_language(self.dfa_odd_length, "Odd Length")

    def check_language(self, dfa, description):
        input_string = self.input_field.get().strip()
        
        # Input validation: Allow only '0', '1', 'a', 'b', 'c'
        if not all(char in '01abc' for char in input_string):
            self.result_label.config(text="Error: Please enter a string containing only '0', '1', 'a', 'b', and 'c'.")
            return

        # Check if the string is accepted by the DFA
        is_accepted = dfa.simulate(input_string)
        result_text = f"Result: {description} - {'Accepted!' if is_accepted else 'Rejected!'}"
        self.result_label.config(text=result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = DFASimulatorApp(root)
    root.mainloop()
