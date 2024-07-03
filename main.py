import os
import time

from InputM import InputM
from encode import Encode

GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"


# encode_state = Encode_TuringMachine_And_States.encode_transition()

class UniversalTuringMachine:
    def __init__(self):
        inputM = InputM()
        encode = Encode()
        self.stateTape = inputM.states  # TM Input State for the simulated TM
        print("self.stateTape : ", self.stateTape)
        self.descriptionTape = inputM.actions  # Description of the simulated TM
        print("self.descriptionTape : ", self.descriptionTape)
        self.contentString = "@" + inputM.input_string + "@"  # Working tape for the simulated TM
        self.contentTape = list(self.contentString)
        print("self.contentTape : ", self.contentTape)
        self.initialState = inputM.start_state  # Initial state of the UTM
        print("self.initialState : ", self.initialState)
        self.stateHead = self.stateTape.index(self.initialState[0])
        print("self.stateHead : ", self.stateHead)
        self.contentHead = 1  # Start at the beginning of the input string (after the initial '@@@')

        self.set_content_head()
        print("self.contentHead : ", self.contentHead)
        self.finalState = inputM.final_state  # Final state of the UTM

    def set_content_head(self):
        for item in self.descriptionTape:
            if item[0] == self.initialState[0]:
                self.descriptionHead = self.initialState[0]
                break

    # a function to check whether the head is at '@' position or not
    # padding with @@@ to mark the beginning and end of the tape.
    def is_threshold(self):
        return self.contentTape[self.contentHead] == '@'

    def show_head(self):
        clear()
        tape_str = ''.join(self.contentTape)
        tape_display = "╔" + "═══╗" * len(tape_str) + "\n"
        tape_display += "║ " + " ║ ".join(tape_str) + " ║\n"
        tape_display += "╚" + "═══╝" * len(tape_str) + "\n"
        head_display = " " + "    " * self.contentHead + " ↑\n"
        print(tape_display + head_display)
        # print(f'Head at position {self.contentHead} reading {self.contentTape[self.contentHead]}')
        # print(f'Current state: {self.stateTape[self.stateHead]}')

    def print_message(self, message):
        print("\n")
        try:
            if message == "ACCEPTED":
                with open("acsi-banners/accept-banner.txt", 'r', encoding='utf-8') as file:
                    content = file.read()
                    print(GREEN + content + RESET)
            else:
                with open("acsi-banners/reject-banner.txt", 'r', encoding='utf-8') as file:
                    content = file.read()
                    print(RED + content + RESET)
        except FileNotFoundError:
            border = "█" * (len(message) + 6)
            print(border)
            print(f"█  {message}  █")
            print(border)

    def step(self):
        if self.stateTape[self.stateHead] in self.finalState:
            self.print_message("ACCEPTED")
            return False

        if self.contentHead + 1 == len(self.contentTape):
            self.contentTape.append("@")
        current_symbol = self.contentTape[self.contentHead]
        # print("current_symbol : ", current_symbol)
        for action in self.descriptionTape:
            # print("action : ", action)
            # print("self.stateTape[self.stateHead] : ", self.stateTape[self.stateHead])
            if action[0] == self.stateTape[self.stateHead] and action[1] == current_symbol:
                self.contentTape[self.contentHead] = action[2]  # Write new symbol
                # print("action[2] : ", action[2])
                self.stateHead = self.stateTape.index(action[4])  # Update state
                self.contentHead += 1 if action[3] == 'R' else -1  # Move head
                time.sleep(0.5)  # Delay for 1 second
                self.show_head()  # Show the tape after the step

                return True

        self.print_message("REJECTED")
        return False

    def run(self):
        self.show_head()
        while self.step():
            pass


def clear():
    os.system('cls')


utm = UniversalTuringMachine()
utm.run()
