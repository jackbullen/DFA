import tkinter as tk
from tkinter import filedialog, messagebox
import json
from collections import defaultdict
import graphviz
class DFA:
    def __init__(self, num_states, accept_states, transitions, alphabet):
        self.num_states = num_states
        self.accept_states = accept_states
        self.transitions = transitions
        self.current_state = 0
        self.states = [i for i in range(self.num_states)]
        self.alphabet = alphabet
    def in_accept_state(self):
        return self.current_state in self.accept_states

    def transition(self, symbol):
        try:
            self.current_state = self.transitions[self.current_state][symbol]
        except KeyError:
            self.current_state = None

class DFA_Visualizer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.num_states_label = tk.Label(self, text="Number of states:")
        self.num_states_entry = tk.Entry(self)
        self.accept_states_label = tk.Label(self, text="Accept states (comma-separated):")
        self.accept_states_entry = tk.Entry(self)
        self.alphabet_label = tk.Label(self, text="Alphabet characters (comma-separated):")
        self.alphabet_entry = tk.Entry(self)
        self.transitions_label = tk.Label(self, text="Transitions (JSON)")
        self.transitions_text = tk.Text(self, height=10, width=30)
        self.create_dfa_button = tk.Button(self, text="Draw DFA", command=self.build_dfa)
        self.test_string_label = tk.Label(self, text="String to test")
        self.test_string_entry = tk.Text(self, height=5, width=30)
        self.test_string_button = tk.Button(self, text="Test string", command=self.test_string)

        self.num_states_label.pack()
        self.num_states_entry.pack()
        self.accept_states_label.pack()
        self.accept_states_entry.pack()
        self.alphabet_label.pack()
        self.alphabet_entry.pack()
        self.transitions_label.pack()
        self.transitions_text.pack()
        self.create_dfa_button.pack()
        self.test_string_button.pack()
        self.test_string_label.pack()
        self.test_string_entry.pack()

    def build_dfa(self):
        try:
            accept_states = set(map(int, self.accept_states_entry.get().strip().split(',')))
            
            delta = json.loads(self.transitions_text.get("1.0", "end").strip())

            alphabet = set(map(str,self.alphabet_entry.get().strip().split(',')))
            
            transitions = defaultdict(dict)
            for state, symbols in delta.items():
                state = int(state)
                for symbol, next_state in symbols.items():
                    next_state = int(next_state)
                    transitions[state][symbol] = next_state

            self.dfa = DFA(int(self.num_states_entry.get().strip()), accept_states, transitions, alphabet)
            self.draw_dfa(self.dfa)
            self.test_string_button.config(state='normal')
        except:
            # print(self.input_field.get("1.0",'end-1c'))
            messagebox.showerror("Error", "Invalid input format.")

    def test_string(self):
        try:
            accept_states = set(map(int, self.accept_states_entry.get().strip().split(',')))
            
            delta = json.loads(self.transitions_text.get("1.0", "end").strip())

            alphabet = set(map(str,self.alphabet_entry.get().strip().split(',')))
            
            transitions = defaultdict(dict)
            for state, symbols in delta.items():
                state = int(state)
                for symbol, next_state in symbols.items():
                    next_state = int(next_state)
                    transitions[state][symbol] = next_state

            self.dfa = DFA(int(self.num_states_entry.get().strip()), accept_states, transitions, alphabet)
            test = self.test_string_entry.get("1.0","end").strip()
            R = [0]
            
            for char in test:

                self.dfa.transition(char)
                R.append(self.dfa.current_state)
            print(R, self.dfa.in_accept_state())
        except:
            messagebox.showerror("Error", "Invalid input format.")


    def draw_dfa(self, dfa):
        # G = nx.DiGraph()
        dot = graphviz.Digraph()
        for state in dfa.states:
            if state in dfa.accept_states:
                dot.node(str(state), shape='circle', style='filled', color='green')
            else:
                dot.node(str(state), shape='circle', style='filled', color='#0ab6fa')
        dot.edge('', '0', arrowhead='normal')
        for state in dfa.states:
            for symbol in dfa.alphabet:
                
                next_state = dfa.transitions[state][symbol]
                # print(symbol, next_state)
                try:
                    if state==next_state:
                        dot.edge(str(state), str(next_state), symbol)
                
                    else:
                        dot.edge(str(state), str(next_state), symbol)
                except KeyError:
                    continue
        dot.render("output", view=True)            

if __name__ == '__main__':
    root = tk.Tk()
    app = DFA_Visualizer(root)
    app.mainloop()

