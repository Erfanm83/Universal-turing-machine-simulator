from InputM import InputM


# encode_state = Encode_TuringMachine_And_States.encode_transition()

class UniversalTuringMachine:
    def __init__(self):
        inputM = InputM()
        self.stateTape = inputM.states  # TM Input State for the simulated TM
        print(self.stateTape)
        self.descriptionTape = inputM.actions  # Description of the simulated TM
        print(self.descriptionTape)
        self.contentTape = inputM.input_string  # Working tape for the simulated TM
        print(self.contentTape)
        self.initialState = inputM.start_state  # Initial state of the UTM
        # print(self.initialState)
        self.stateHead = self.stateTape.index(self.initialState[0])
        print(self.initialState[0])
        self.descriptionHead = 0
        self.contentHead = 0
        self.finalState = inputM.final_state  # Final state of the UTM

utm = UniversalTuringMachine()
