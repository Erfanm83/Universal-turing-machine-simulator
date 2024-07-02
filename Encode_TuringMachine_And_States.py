from InputM import InputM

blank = '#'

inputM = InputM()
states = inputM.states
start_state = inputM.start_state
final_state = inputM.final_state
actions = inputM.actions


def encode_transition(states1, start_state1, final_state1, actions1):
    encode_array_states = []
    tuple_states = []
    x = 1
    len_states = len(states1)
    for i in range(len_states):
        for j in range(x):
            encode_array_states.append(1)
        tuple_states.append({states1[i]: x})

        x += 1
        encode_array_states.append(0)
    encode_array_states.pop(len(encode_array_states) - 1)

    array_action = []

    for action in actions1:
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

    yield encode_array_states
    yield array_action
