import os
import time

from InputM import InputM
from encode import Encode

# ANSI color codes for terminal text formatting
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"
blank = "#"
spliter = "$"
speed = 0

class UniversalTuringMachine:
    def __init__(self):
        encode = Encode()
        inputM = InputM()
        self.descriptionHead = None
        self.stateTape = encode.string_states  # TM Input States for the simulated TM
        self.descriptionTape = encode.string_describe  # Description of the simulated TM
        self.contentString = blank + inputM.input_string + blank  # Working tape for the simulated TM
        self.contentTape = list(self.contentString)  # Convert content string to list
        self.initialState = encode.decode_start()  # Initial state of the UTM
        self.stateHead = self.stateTape.index(self.initialState)  # Head position in state tape
        self.contentHead = 1  # Start at the beginning of the input string (after the initial blank)
        self.set_content_head()
        self.finalState = encode.decode_final()  # Final state of the UTM
        # Create ShowTape object with current instance as a parameter
        self.showTape = ShowTape(self)
        # self.stateHead = 0

    def set_content_head(self):
        koja = 0
        x = 0
        for item in self.descriptionTape.split("$"):
            tedad = 0
            it = item.split("0")
            if it[0] == self.initialState and self.get_ASCI_letter(it[1]) == self.contentTape[1]:
                break
            # if it[0] == "1":
            #     break
            x += 1
        koja += x
        for item in self.descriptionTape.split("$"):
            if x != 0:
                koja += len(item)
                x -= 1
            else:
                break
        self.descriptionHead = koja
        return koja
        # print("self.descriptionHead : " , self.descriptionHead)

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
        if self.contentHead + 1 == len(self.contentTape):
            self.contentTape.append(blank)

        elif self.contentTape[self.contentHead] == blank:
            self.contentTape = [blank] + self.contentTape
            self.contentHead += 1

        current_symbol = self.contentTape[self.contentHead]
        for action in self.descriptionTape.split("$"):
            current_action = action.split("0")
            if self.stateTape.index(current_action[0]) == self.stateHead and self.get_ASCI_letter(
                    current_action[1]) == current_symbol:
                self.descriptionHead = self.set_content_head()
                self.contentTape[self.contentHead] = self.get_ASCI_letter(current_action[2])  # Write new symbol
                self.stateHead = self.stateTape.index(current_action[4])  # Update state
                self.contentHead += 1 if current_action[3] == '11' else -1  # Move head
                time.sleep(speed)  # Delay for 0.5 seconds
                self.showTape.show_head()
                return True

        if self.stateHead == self.stateTape.index(self.finalState):
            self.showTape.show_head()
            self.print_message("ACCEPTED")
            return False
        self.showTape.show_head()
        self.print_message("REJECTED")
        return False

    def run(self):
        # Run the Turing machine until it halts
        self.showTape.show_head()
        while self.step():
            pass

    def get_ASCI_letter(self, letter):
        return chr(len(letter))


class ShowTape:
    def __init__(self, utm_instance):
        self.utm = utm_instance

    def show_head(self):
        # Clear the console and display the content tape with the head position
        clear()
        print("Content Tape : ")
        tape_str = ''.join(self.utm.contentTape)
        tape_display = "╔" + "═══╗" * len(tape_str) + "\n"
        tape_display += "║ " + " ║ ".join(tape_str) + " ║\n"
        tape_display += "╚" + "═══╝" * len(tape_str) + "\n"
        head_display = " " + "    " * self.utm.contentHead + " ↑\n"
        print(tape_display + head_display)

        self.draw_tape("State Tape", self.utm.stateTape, self.utm.stateHead)
        self.draw_tape("Description Tape", self.utm.descriptionTape, self.utm.descriptionHead)
        # self.show_state_head()

    def show_state_head(self):
        # Display the state tape with the head position
        print("State Tape : ")
        tapelength = max(len(string) for string in self.utm.stateTape)
        tape_str = ''.join(self.utm.stateTape)
        tape_display = "╔" + ("═" * tapelength + "══╗") * len(self.utm.stateTape) + "\n"
        tape_display += "║ " + " ║ ".join(self.utm.stateTape[i] for i in range(0, len(self.utm.stateTape))) + " ║\n"
        tape_display += "╚" + ("═" * tapelength + "══╝") * len(self.utm.stateTape) + "\n"
        space_threshold = len(tape_display) // 3 // len(self.utm.stateTape)
        head_display = " " * space_threshold * self.utm.stateHead + " " * (self.utm.stateHead) + " ↑\n"
        print(tape_display + head_display)

        # self.show_description_head()

    def show_description_head(self):
        # Display the description tape with the head position
        print("Description Tape : ")
        # Flatten the description tape with '%' symbol between each sublist
        flattened_list = [item for sublist in self.utm.descriptionTape for item in sublist + ['$']]
        flattened_list.pop()  # Remove the last '%'
        description_str = ','.join(flattened_list).replace('$', ', $ ,')
        tapelength = max(len(string) for string in description_str.split(', $ ,'))
        tape_segments = description_str.split(', $ ,')
        tape_display = "╔" + ("═" * (tapelength + 1) + "╗") * len(tape_segments) + "\n"
        tape_display += "║" + " ║".join(segment.center(tapelength) for segment in tape_segments) + " ║\n"
        tape_display += "╚" + ("═" * (tapelength + 1) + "╝") * len(tape_segments) + "\n"

        head_display = "       " + " " * (tapelength + 2) * self.utm.descriptionHead + " ↑\n"

        print(tape_display + head_display)

    def draw_tape(self, tapeName, tape_string, head):
        print(tapeName + " : ")
        # Construct the top border of the tape
        top_border = "╔" + "═══╗" * len(tape_string)

        # Construct the middle part with each character in its cell
        middle_part = "║ " + " ║ ".join(tape_string) + " ║"

        # Construct the bottom border of the tape
        bottom_border = "╚" + "═══╝" * len(tape_string)

        head_display = "    " * head + "  ↑\n"
        # Print the tape
        print(top_border)
        print(middle_part)
        print(bottom_border)
        print(head_display)


def clear():
    # Clear the console (works for Windows)
    os.system('cls')

utm = UniversalTuringMachine()
utm.run()