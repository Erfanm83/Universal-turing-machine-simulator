from InputM import InputM

blank = '#'

inputM = InputM()
states_input = inputM.states
start_state_input = inputM.start_state
final_state_input = inputM.final_state
actions_input = inputM.actions


class Decode:
    def __init__(self):
        self.array_states = []
        self.array_action = []

        self.describe = []
        self.__states = states_input
        self.__actions = actions_input
        self.__start_state = start_state_input
        self.__final_state = final_state_input
        self.__encode_state()
        self.__encode_action()
        self.__describe_TM()

    def __encode_state(self):
        encode_array_states = []
        tuple_states = []

        x = 1
        len_states = len(self.__states)
        for i in range(len_states):
            for j in range(x):
                encode_array_states.append(1)
            tuple_states.append({self.__states[i]: x})

            x += 1
            encode_array_states.append(0)
        encode_array_states.pop(len(encode_array_states) - 1)
        self.dictionaries_state = tuple_states
        self.array_states = encode_array_states

    def __encode_action(self):
        array_action = []
        for action in self.__actions:
            for tple_state in self.dictionaries_state:
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

            for tple_state in self.dictionaries_state:
                if tple_state.get(action[4]) is not None:
                    for i in range(tple_state.get(action[4])):
                        array_action.append(1)
                    array_action.append(0)

            array_action.append('$')

        array_action.pop(len(array_action) - 1)

        self.array_action = array_action

    def __describe_TM(self):
        array_decribe = []
        for action in self.__actions:
            for tple_state in self.dictionaries_state:
                if tple_state.get(action[0]) is not None:
                    for i in range(tple_state.get(action[0])):
                        array_decribe.append(1)
                    array_decribe.append(0)

            if action[1] != 'blank':
                for i in range(ord(action[1])):
                    array_decribe.append(1)
                array_decribe.append(0)
            else:
                array_decribe.append("#")
                array_decribe.append(0)

            if action[2] != 'blank':
                for i in range(ord(action[2])):
                    array_decribe.append(1)
                array_decribe.append(0)
            else:
                array_decribe.append("#")
                array_decribe.append(0)

            if action[3] == 'l' or action[3] == 'L':
                array_decribe.append(1)
                array_decribe.append(0)
            elif action[3] == 'r' or action[3] == 'R':
                array_decribe.append(1)
                array_decribe.append(1)
                array_decribe.append(0)

            for tple_state in self.dictionaries_state:
                if tple_state.get(action[4]) is not None:
                    for i in range(tple_state.get(action[4])):
                        array_decribe.append(1)
                    array_decribe.append(0)

            array_decribe.pop(len(array_decribe) - 1)
            array_decribe.append('$')

        self.describe = array_decribe

    def decode_state(self, arr):
        for state_dict in self.dictionaries_state:
            for state_name, value in state_dict.items():
                if state_name == arr:
                    return value

        return 0


# # Example
# decode = Decode()
# action = decode.array_action
# states = decode.array_states
#
# number_start_state = decode.decode_state(start_state_input[0])
# number_final_state = decode.decode_state(final_state_input[0])
# var = decode.describe
