# aoc_state_machine.py

from dataclasses import dataclass
import numpy as np
from datetime import datetime

@dataclass
class LogicGates:
    memory: dict[str, int]
    program: list[str]

    def get_gate(self, wire):
        return self.memory[wire]
    
    def test_gate(self, wire):
        return wire in self.memory

    def run(self):
        """Run the program"""
        current_line = 0
        while current_line < len(self.program):
            instruction = self.program[current_line]

            # Set a register to a value
            if instruction[0].startswith("NOT"):
                if instruction[0].split()[1] in self.memory:
                    temp = self.memory[instruction[0].split()[1]]
                    if str(temp).isdigit():
                        self.memory[instruction[-1]] = ~np.uint16(temp)

            elif instruction[0].__contains__("AND"):
                x, _, y = instruction[0].split()
                if x.isalpha():
                    x = self.memory[x] if x in self.memory else '.'
                
                if y.isalpha():
                    y = self.memory[y] if y in self.memory else '.'

                if str(x).isdigit() and str(y).isdigit():
                    self.memory[instruction[-1]] = np.uint16(x) & np.uint16(y)

            elif instruction[0].__contains__("OR"):
                x, _, y = instruction[0].split()
                if x.isalpha():
                    x = self.memory[x] if x in self.memory else '.'
                
                if y.isalpha():
                    y = self.memory[y] if y in self.memory else '.'

                if str(x).isdigit() and str(y).isdigit():
                    self.memory[instruction[-1]] = np.uint16(x) | np.uint16(y)

            elif instruction[0].__contains__("LSHIFT"):
                x, _, y = instruction[0].split()
                if x.isalpha():
                    x = self.memory[x] if x in self.memory else '.'
                
                if y.isalpha():
                    y = self.memory[y] if y in self.memory else '.'

                if str(x).isdigit() and str(y).isdigit():
                    self.memory[instruction[-1]] = np.uint16(x) << np.uint16(y)
                    
            elif instruction[0].__contains__("RSHIFT"):
                x, _, y = instruction[0].split()
                if x.isalpha():
                    x = self.memory[x] if x in self.memory else '.'
                
                if y.isalpha():
                    y = self.memory[y] if y in self.memory else '.'

                if str(x).isdigit() and str(y).isdigit():
                    self.memory[instruction[-1]] = np.uint16(x) >> np.uint16(y)

            else: # just a set operation
                if len(instruction) == 2:
                    x, y = instruction
                    x = self.memory[x] if x in self.memory else '.'

                    if type(x) is np.uint16:
                        self.memory[y] = np.uint16(x)

            # Move the line pointer
            current_line += 1
