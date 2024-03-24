class MarsRover:
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation.strip()
        self.lost = False

    def move_forward(self):
        if self.orientation == 'N':
            self.y += 1
        elif self.orientation == 'E':
            self.x += 1
        elif self.orientation == 'S':
            self.y -= 1
        elif self.orientation == 'W':
            self.x -= 1

    def rotate_left(self):
        if self.orientation == 'N':
            self.orientation = 'W'
        elif self.orientation == 'E':
            self.orientation = 'N'
        elif self.orientation == 'S':
            self.orientation = 'E'
        elif self.orientation == 'W':
            self.orientation = 'S'

    def rotate_right(self):
        if self.orientation == 'N':
            self.orientation = 'E'
        elif self.orientation == 'E':
            self.orientation = 'S'
        elif self.orientation == 'S':
            self.orientation = 'W'
        elif self.orientation == 'W':
            self.orientation = 'N'

    def execute_commands(self, commands, grid):
        for command in commands:
            if command == 'F':
                new_x = self.x
                new_y = self.y

                if self.orientation == 'N':
                    new_y += 1
                elif self.orientation == 'E':
                    new_x += 1
                elif self.orientation == 'S':
                    new_y -= 1
                elif self.orientation == 'W':
                    new_x -= 1

                if 0 <= new_x <= grid[0] and 0 <= new_y <= grid[1]:
                    self.x = new_x
                    self.y = new_y
                else:
                    self.lost = True
                    break
            elif command == 'L':
                self.rotate_left()
            elif command == 'R':
                self.rotate_right()

        return self

def process_input(input_str):
    input_lines = input_str.strip().split('\n')
    grid = tuple(map(int, input_lines[0].split()))
    rovers = []

    for line in input_lines[1:]:
        line_parts = line.split(") ")
        x, y, orientation = line_parts[0].strip('()').split(',')
        commands = line_parts[1]
        rovers.append(MarsRover(int(x), int(y), orientation).execute_commands(commands, grid))

    return rovers

def format_output(rovers):
    output_lines = []

    for rover in rovers:
        if rover.lost:
            output_lines.append(f"({rover.x}, {rover.y}, {rover.orientation}) LOST")
        else:
            output_lines.append(f"({rover.x}, {rover.y}, {rover.orientation})")

    return '\n'.join(output_lines)

input_str = '''4 8
(2, 3, N) FLLFR
(1, 0, S) FFRLF'''


rovers = process_input(input_str)
output_str = format_output(rovers)
print(output_str)