class UniversalTuringMachine:
    def __init__(self):
        self.tape1 = []  # Description of the simulated TM
        self.tape2 = []  # Input for the simulated TM
        self.tape3 = []  # Working tape for the simulated TM
        self.head1 = 0
        self.head2 = 0
        self.head3 = 0
        self.state = 'q0'  # Initial state of the UTM

    def read_tm_from_file(self, filename):
        # Read TM description from file and convert to binary
        # This is a simplified version
        with open(filename, 'r') as file:
            tm_description = file.read().strip()
        self.tape1 = [int(bit) for bit in self.convert_to_binary(tm_description)]

    def convert_to_binary(self, tm_description):
        # Convert TM description to binary (simplified)
        return ''.join(format(ord(char), '08b') for char in tm_description)

    def set_input(self, input_string):
        self.tape2 = list(input_string)

    def step(self):
        if self.state == 'q0':
            # Read from tape1 and tape2, write to tape3
            if self.head1 < len(self.tape1) and self.head2 < len(self.tape2):
                self.tape3.append(self.tape2[self.head2])
                self.head1 += 1
                self.head2 += 1
                self.head3 += 1
            else:
                self.state = 'q1'
        elif self.state == 'q1':
            # Simulate the TM described on tape1 using tape3
            # This is where the main logic of the UTM would go
            # For simplicity, we'll just move right on tape3
            if self.head3 < len(self.tape3):
                self.head3 += 1
            else:
                self.state = 'qf'  # Final state

    def run(self):
        while self.state != 'qf':
            self.step()

    def get_output(self):
        return ''.join(self.tape3)


# Example usage
utm = UniversalTuringMachine()
utm.read_tm_from_file('utm-des.txt')  # Assume this file contains a TM description
utm.set_input('1101')
utm.run()
print(utm.get_output())
