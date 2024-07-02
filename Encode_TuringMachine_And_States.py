from InputM import InputM

blank = '#'

inputM = InputM()
states = inputM.states
start_state = inputM.start_state
final_state = inputM.final_state
actions = inputM.actions


class Decode:
    def __init__(self):
        self.array_states = []
        self.array_action = []
        self.states1 = states
        self.actions1 = actions
        self.start_state1 = start_state
        self.final_state1 = final_state
        self._encod()

    def _encod(self):
        # self.encode_array_states = encode_transition(states, start_state, final_state, actions)
        # self.array_action = encode_transition(states, start_state, final_state, actions)

        encode_array_states = []
        tuple_states = []
        x = 1
        len_states = len(self.states1)
        for i in range(len_states):
            for j in range(x):
                encode_array_states.append(1)
            tuple_states.append({self.states1[i]: x})

            x += 1
            encode_array_states.append(0)
        encode_array_states.pop(len(encode_array_states) - 1)
        self.array_states = encode_array_states

        array_action = []

        for action in self.actions1:
            for tple_state in tuple_states:
                if tple_state.get(action[0]) is not None:
                    for i in range(tple_state.get(action[0])):
                        array_action.append(1)
                    array_action.append(0)

            if action[1] != 'blank':
                array_action.append(action[1])
                array_action.append(0)
            else:
                array_action.append("#")
                array_action.append(0)

            if action[2] != 'blank':
                array_action.append(action[2])
                array_action.append(0)
            else:
                array_action.append("#")
                array_action.append(0)

            if action[3] == 'l' or action[3] == 'L':
                array_action.append(1)
                array_action.append(0)
            elif action[3] == 'r' or action[3] == 'R':
                array_action.append(1)
                array_action.append(1)
                array_action.append(0)

            for tple_state in tuple_states:
                if tple_state.get(action[4]) is not None:
                    for i in range(tple_state.get(action[4])):
                        array_action.append(1)
                    array_action.append(0)

            array_action.append('$')

        array_action.pop(len(array_action) - 1)

        self.array_action = array_action