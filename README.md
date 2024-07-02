# Universal Turing Machine Project

## Overview

This project implements a Universal Turing Machine (UTM) that can simulate any given Turing machine. The UTM has three tapes: one for the description of the Turing machine, one for internal states, and one for the input string. The UTM reads the encoded description of the Turing machine, decodes it, and then simulates the machine on the given input string.

## Project Structure

- **TuringMachineEncoderDecoder Class**: This class is responsible for encoding the Turing machine description into an ASCII string and decoding it back into the description.
- **Tape Class**: This class simulates a Turing machine tape with methods to read, write, and move the head.
- **UniversalTuringMachine Class**: This class defines the UTM with three tapes and includes methods to parse the description, execute steps, and run the Turing machine.

## Files

- `utm.py`: Contains the implementation of the TuringMachineEncoderDecoder, Tape, and UniversalTuringMachine classes.
- `README.md`: This file, providing an overview of the project.

## Encoding and Decoding the Turing Machine Description

### Example Turing Machine Description

```plaintext
states: {q1,q2,q0,q4}
start_state: {q0}
final_states: {q4}
actions: {(q0,1,x,R,q0),(q0,blank,blank,L,q1),(q1,1,1,L,q1),(q1,x,1,R,q2),(q2,1,1,R,q2),(q2,blank,1,L,q1),(q1,blank,blank,R,q4)}

### Encoding Format

The transition functions are encoded into an ASCII string separated by a symbol (e.g., `#`). For example, the action `(q0,1,x,R,q0)` is encoded as `0#1#88#82#0#...`.

### Example Usage

#### Encoding

```python
states = {'q1', 'q2', 'q0', 'q4'}
start_state = 'q0'
final_states = {'q4'}
actions = [
    ('q0', '1', 'x', 'R', 'q0'),
    ('q0', ' ', ' ', 'L', 'q1'),
    ('q1', '1', '1', 'L', 'q1'),
    ('q1', 'x', '1', 'R', 'q2'),
    ('q2', '1', '1', 'R', 'q2'),
    ('q2', ' ', '1', 'L', 'q1'),
    ('q1', ' ', ' ', 'R', 'q4')
]

encoder_decoder = TuringMachineEncoderDecoder(states, start_state, final_states, actions)
encoded_string = encoder_decoder.encode()
print("Encoded String:", encoded_string)
