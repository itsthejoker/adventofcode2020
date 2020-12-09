from data import load_data

input = load_data()

input = input.split('\n')


class Computer:
    def __init__(self):
        self.program = None
        self.accumulator = 0
        self.current_line = 0
        self.executed_lines = []
        self.iteration_count = 0

    def get_instruction_num(self, specific_line_no=None):
        if specific_line_no:
            return int(self.program[specific_line_no].split()[1])
        return int(self.program[self.current_line].split()[1])

    def reset(self):
        self.accumulator = 0
        self.current_line = 0
        self.executed_lines = []
        self.iteration_count = 0

    def execute_program(self, stop_after=None):
        while True:
            if stop_after:
                if self.iteration_count > stop_after:
                    print(f"Reached end of execution. {self.accumulator=}, {self.iteration_count=}")
                    break
            if self.current_line in self.executed_lines:
                raise Exception(
                    f"Loop detected! {self.current_line=}, {self.accumulator=}, {self.iteration_count=}"
                )
            if self.current_line >= len(self.program):
                print(f"Reached end of execution. {self.accumulator=}, {self.iteration_count=}")
                break
            line, line_no = self.program[self.current_line], self.current_line
            if "nop" in line:
                self.current_line += 1
            elif "acc" in line:
                self.accumulator += self.get_instruction_num()
                self.current_line += 1
            elif "jmp" in line:
                self.current_line += self.get_instruction_num()
            self.executed_lines.append(line_no)
            self.iteration_count += 1

    def load(self, program):
        self.program = {c: i for c, i in enumerate(program) if i != ""}


computer = Computer()
computer.load(input)
try:
    computer.execute_program()
except Exception as e:
    print(f"Part 1: {e}")

instructions = [i for i, c in computer.program.items() if "nop" in c or "jmp" in c]

for line in instructions:
    stored_instruction = computer.program[line]
    new_inst = "nop" if "jmp" in stored_instruction else "jmp"
    # print(f"Replacing {stored_instruction=} with {new_inst}")
    computer.program[line] = f"{new_inst} {computer.get_instruction_num(specific_line_no=line)}"
    try:
        computer.reset()
        computer.execute_program()
        print(f"Execution succeeded, changed {line=}, {computer.accumulator=}")
        break
    except Exception as e:
        pass
    computer.program[line] = stored_instruction

print("END OF LINE.")
