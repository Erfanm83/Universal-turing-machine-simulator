import re

address = "test/one_aa_TM.txt"
input_address = "test/one_aa_input_reject.txt"
blank = "#"


class InputM:
    def __init__(self):
        """
    Reads two files (inputstr.txt and inputMachine.txt) from the specified folder
    and stores the contents in the class fields.
    """
        self.states = []
        self.start_state = []
        self.final_state = []
        self.actions = []

        self._read_file()
        self._read_input_string()

    def _read_file(self):
        """
        Reads a file and parses the information specific to the inputMachine.txt format.
    """
        with open(address, "r") as f:
            for line in f:
                key, value = line.replace(" ", "").strip().split(":", 1)
                value = value.strip()[1:-1].split(",")  # Remove curly braces and split by comma
                if key == "States":
                    self.states = value
                elif key == "StartState":
                    self.start_state = value
                elif key == "FinalStates":
                    self.final_state = value
                elif key == "Actions":
                    transitions = line.replace(" ", "").strip().split(":")[1].strip()[1:-1]
                    self.actions = self._parse_actions(transitions)

    def _read_input_string(self):
        """
    Reads the input string from the inputstr.txt file.
    """
        with open(input_address, "r") as f:
            self.input_string = f.readline().replace(" ", "").strip()  # Assuming single line input string

    def _parse_actions(self, str):

        """
        Parses the actions string into a list of lists without using eval.
        """
        pattern = r'\((.*?)\)'

        # Find all matches using re.findall
        matches = re.findall(pattern, str)

        # Create a list to hold the extracted substrings
        result_list = []

        # Add each match to the result list
        for match in matches:
            sub_list = match.strip().replace("blank", blank).split(",")
            result_list.append(sub_list)
            
        return result_list

# Example usage
# inputM = InputM()

# print(inputM.states)  # Output: ['q1', 'q2', 'q0', 'q4']
# print(inputM.start_state)  # Output: ['q0']
# print(inputM.final_state)  # Output: ['q4']
# print(inputM.actions)
# print(inputM.actions[0])  # Output: ['q0', '1', 'x', 'R', 'q0']
# print(inputM.actions[0][0])  # Output: q0