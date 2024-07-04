from InputM import InputM

blank = '#'

inputM = InputM()
states_input = inputM.states
start_state_input = inputM.start_state
final_state_input = inputM.final_state
actions_input = inputM.actions


class Encode:
    def __init__(self):
        self.array_states = []
        self.array_action = []
        self.describe = []

        self.__string_machine = ""
        self.__states = states_input
        self.__actions = actions_input
        self.__start_state = start_state_input
        self.__final_state = final_state_input
        self.__encode_state()
        self.__encode_action()
        self.__describe_TM()
        self.__tuple_states = []

    def __encode_state(self):
        encode_array_states = []
        tuple_states = []

        x = 1
        len_states = len(self.__states)
        for i in range(len_states):
            temp = ""
            for j in range(x):
                temp += "1"
            encode_array_states.append(temp)
            tuple_states.append({self.__states[i]: x})
            x += 1
            # encode_array_states.append(0)
        # encode_array_states.pop(len(encode_array_states) - 1)

        # print("encode_array_states ", encode_array_states)
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
        for act in self.__actions:
            for tple_state in self.dictionaries_state:
                if tple_state.get(act[0]) is not None:
                    for i in range(tple_state.get(act[0])):
                        array_decribe.append(1)
                        self.__string_machine += "1"
                    array_decribe.append(0)
                    self.__string_machine += "0"

            if act[1] != 'blank':
                for i in range(ord(act[1])):
                    array_decribe.append(1)
                    self.__string_machine += "1"
                array_decribe.append(0)
                self.__string_machine += "0"
            else:
                array_decribe.append("#")
                self.__string_machine += "#"
                array_decribe.append(0)
                self.__string_machine += "0"

            if act[2] != 'blank':
                for i in range(ord(act[2])):
                    array_decribe.append(1)
                    self.__string_machine += "1"
                array_decribe.append(0)
                self.__string_machine += "0"
            else:
                array_decribe.append("#")
                self.__string_machine += "#"
                array_decribe.append(0)
                self.__string_machine += "0"

            if act[3] == 'l' or act[3] == 'L':
                array_decribe.append(1)
                self.__string_machine += "1"
                array_decribe.append(0)
                self.__string_machine += "0"
            elif act[3] == 'r' or act[3] == 'R':
                array_decribe.append(1)
                self.__string_machine += "1"
                array_decribe.append(1)
                self.__string_machine += "1"
                array_decribe.append(0)
                self.__string_machine += "0"

            for tple_state in self.dictionaries_state:
                if tple_state.get(act[4]) is not None:
                    for i in range(tple_state.get(act[4])):
                        array_decribe.append(1)
                        self.__string_machine += "1"
                    array_decribe.append(0)
                    self.__string_machine += "0"

            array_decribe.pop(len(array_decribe) - 1)
            array_decribe.append('$')
            self.__string_machine += "$"

        self.describe = array_decribe
        # print(self.__string_machine)

    def decode_state(self, arr):
        for state_dict in self.dictionaries_state:
            for state_name, value in state_dict.items():
                if state_name == arr:
                    str = ""
                    for i in range(value):
                        str += "1"
                    return str

        return 0

    def decode_start(self):
        return self.decode_state(start_state_input[0])

    def decode_final(self):
        return self.decode_state(final_state_input[0])

    def array_encode(self, state, input):
        st = self.decode_state(state)
        compare_state = ""
        for i in range(st):
            compare_state += "1"
        inp = ord(input)
        compare_input = ""
        for i in range(inp):
            compare_input += "1"

        str_MT = self.__string_machine.split("$")

        for acts in str_MT:
            act = acts.split("0")
            if act[0] == compare_state:
                if act[1] == compare_input:
                    x = len(act[2])
                    out_put = chr(x)

                    L_or_R = ""
                    if len(act[3]) == 2:
                        L_or_R = "R"
                    elif len(act[3]) == 1:
                        L_or_R = "L"

                    next_state = ""
                    for dict in self.dictionaries_state:
                        for name, val in dict.items():
                            if val == len(act[4]):
                                next_state = name
                                break

                    return out_put, L_or_R, next_state

        return 0

    def input_state(self, state, input):
        q_state = ""
        for dict in self.dictionaries_state:
            for name, val in dict.items():
                if val == len(state):
                    q_state = name
                    break
        string_input = chr(len(input))

        return q_state, string_input

# Example
# encode = Encode()


# print(encode.decode_final())
# action = encode.array_action
# print(action)
# states = encode.array_states
# print(states)
#
# number_start_state = encode.decode_state(start_state_input[0])
# number_final_state = encode.decode_state(final_state_input[0])
# print(number_start_state)
# print(number_final_state)
#
# descr = encode.describe
# print(descr)
#
#
# q, inp = encode.input_state("111","11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
# print(q, inp)

# print(encode.array_encode(q, inp))

# q, inp = encode.input_state("111","1111111111111111111111111111111111111111111111111")
# print(q, inp)

# print(encode.array_encode(q, inp))

# print(encode.array_encode("q0", "b"))
