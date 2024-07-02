from InputM import InputM


class UniversalTuringMachine:
    def __init__(self):
        inputM = InputM()
        self.stateTape = inputM.states  # TM Input State for the simulated TM
        self.descriptionTape = inputM.actions  # Description of the simulated TM
        self.contentTape = inputM.input_string  # Working tape for the simulated TM
        self.stateHead = 0
        self.descriptionHead = 0
        self.contentHead = 0
        self.initialState = inputM.start_state  # Initial state of the UTM
        self.finalState = inputM.final_state  # Final state of the UTM


utm = UniversalTuringMachine()
