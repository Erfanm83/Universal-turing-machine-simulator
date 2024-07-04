import os
import time

from InputM import InputM

# ANSI color codes for terminal text formatting
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"
blank = "#"

class UniversalTuringMachine:
    def __init__(self):
        self.descriptionHead = None
        inputM = InputM()
        self.stateTape = inputM.states  # TM Input States for the simulated TM
        print("self.stateTape : ", self.stateTape)
        self.descriptionTape = inputM.actions  # Description of the simulated TM
        print("self.descriptionTape : ", self.descriptionTape)
        self.contentString = blank + inputM.input_string + blank  # Working tape for the simulated TM
        self.contentTape = list(self.contentString)  # Convert content string to list
        print("self.contentTape : ", self.contentTape)
        self.initialState = inputM.start_state  # Initial state of the UTM
        print("self.initialState : ", self.initialState)
        self.stateHead = self.stateTape.index(self.initialState[0])  # Head position in state tape
        print("self.stateHead : ", self.stateHead)
        self.contentHead = 1  # Start at the beginning of the input string (after the initial blank)

        self.set_content_head()
        print("self.contentHead : ", self.contentHead)
        self.finalState = inputM.final_state  # Final state of the UTM

    def set_content_head(self):
        # Set the initial description head based on the initial state and input symbol
        for item in self.descriptionTape:
            if item[0] == self.initialState[0] and item[1] == self.contentTape[1]:
                self.descriptionHead = self.descriptionTape.index(item)
                break

    def is_threshold(self):
        # Check if the head is at the blank position
        return self.contentTape[self.contentHead] == blank

    def show_head(self):
        # Clear the console and display the content tape with the head position
        clear()
        print("Content Tape : ")
        tape_str = ''.join(self.contentTape)
        tape_display = "╔" + "═══╗" * len(tape_str) + "\n"
        tape_display += "║ " + " ║ ".join(tape_str) + " ║\n"
        tape_display += "╚" + "═══╝" * len(tape_str) + "\n"
        head_display = " " + "    " * self.contentHead + " ↑\n"
        print(tape_display + head_display)

        self.show_state_head()

    def show_state_head(self):
        # Display the state tape with the head position
        print("State Tape : ")
        tapelength = max(len(string) for string in self.stateTape)
        tape_str = ''.join(self.stateTape)
        tape_display = "╔" + ("═" * tapelength + "══╗") * len(self.stateTape) + "\n"
        tape_display += "║ " + " ║ ".join(self.stateTape[i] for i in range(0, len(self.stateTape))) + " ║\n"
        tape_display += "╚" + ("═" * tapelength + "══╝") * len(self.stateTape) + "\n"
        head_display = " " + " " * (tapelength + 1) * tapelength * self.stateHead + " ↑\n"
        print(tape_display + head_display)

        self.show_description_head()

    def show_description_head(self):
        # Display the description tape with the head position
        print("Description Tape : ")
        # Flatten the description tape with '%' symbol between each sublist
        flattened_list = [item for sublist in self.descriptionTape for item in sublist + ['%']]
        flattened_list.pop()  # Remove the last '%'
        description_str = ','.join(flattened_list).replace('%', ', % ,')
        tapelength = max(len(string) for string in description_str.split(', % ,'))
        tape_segments = description_str.split(', % ,')
        tape_display = "╔" + ("═" * (tapelength + 1) + "╗") * len(tape_segments) + "\n"
        tape_display += "║" + " ║".join(segment.center(tapelength) for segment in tape_segments) + " ║\n"
        tape_display += "╚" + ("═" * (tapelength + 1) + "╝") * len(tape_segments) + "\n"

        head_display = "       " + " " * (tapelength + 2) * self.descriptionHead + " ↑\n"

        print(tape_display + head_display)

    def print_message(self, message):
        # Print the acceptance or rejection message
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
        # Perform one step of the Turing machine computation
        if self.stateTape[self.stateHead] in self.finalState:
            self.print_message("ACCEPTED")
            return False

        if self.contentHead + 1 == len(self.contentTape):
            self.contentTape.append(blank)
        # elif self.contentHead - 1 < 0:
        #     contentList = list("@")
        #     self.contentTape = contentList.append(self.contentTape)
        current_symbol = self.contentTape[self.contentHead]
        for action in self.descriptionTape:
            if action[0] == self.stateTape[self.stateHead] and action[1] == current_symbol:
                self.descriptionHead = self.descriptionTape.index(action)
                self.show_head()  # Show the tape after the step
                self.contentTape[self.contentHead] = action[2]  # Write new symbol
                self.stateHead = self.stateTape.index(action[4])  # Update state
                self.contentHead += 1 if action[3] == 'R' else -1  # Move head
                time.sleep(0.5)  # Delay for 0.5 seconds

                return True
        self.print_message("REJECTED")
        return False

    def run(self):
        # Run the Turing machine until it halts
        self.show_head()
        while self.step():
            pass

def clear():
    # Clear the console (works for Windows)
    os.system('cls')


# Instantiate and run the Universal Turing Machine
utm = UniversalTuringMachine()
utm.run()
