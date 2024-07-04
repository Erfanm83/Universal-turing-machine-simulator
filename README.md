# Universal Turing Machine Project

## Overview

This project implements a Universal Turing Machine (UTM) that can simulate any given Turing machine. The UTM has three tapes: one for the description of the Turing machine, one for internal states, and one for the input string. The UTM reads the encoded description of the Turing machine, decodes it, and then simulates the machine on the given input string.

## Project Structure

- **TuringMachineEncoderDecoder Class**: This class is responsible for encoding the Turing machine description into an ASCII string and decoding it back into the description.
- **Tape Class**: This class simulates a Turing machine tape with methods to read, write, and move the head.
- **UniversalTuringMachine Class**: This class defines the UTM with three tapes and includes methods to parse the description, execute steps, and run the Turing machine.

## Files

- `InputM.py`: Contains the `InputM` class for defining the input string and machine states.
- `encode.py`: Contains the `Encode` class for encoding and decoding the Turing machine descriptions.
- `utm.py`: Contains the implementation of the `UniversalTuringMachine` and `ShowTape` classes with graphical representation using Tkinter.
- `main.py`: The entry point for running the Universal Turing Machine.
- `README.md`: This file, providing an overview of the project.
- `acsi-banners/`: Directory containing ASCII art for acceptance and rejection messages.

## Encoding and Decoding the Turing Machine Description

### Example Turing Machine Description

```plaintext
states: {q1,q2,q0,q4}
start_state: {q0}
final_states: {q4}
actions: {(q0,1,x,R,q0),(q0,blank,blank,L,q1),(q1,1,1,L,q1),(q1,x,1,R,q2),(q2,1,1,R,q2),(q2,blank,1,L,q1),(q1,blank,blank,R,q4)}
```
### Encoding Format

The transition functions are encoded into an ASCII string separated by a symbol (e.g., `#`). For example, the action `(q0,1,x,R,q0)` is encoded as `0#1#88#82#0#...`.

### Example Usage

#### Encoding
Put This Stuff on a .txt file on `input` folder or `test` folder then note that on `InputM.py` file you should have change the address 
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
```
on the `utm.py` file you can change the speed of the output on the section named `os.sleep`
