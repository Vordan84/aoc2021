
from pathlib import Path

INPUT_FILE = 'input.txt'

filePath = Path(__file__).with_name(INPUT_FILE)
with filePath.open('r') as input:
    lines = input.readlines()

    position = 0
    depth = 0
    aim = 0

    for line in lines:
        command = line.split()
        direction = command[0]
        velocity = int(command[1])

        if direction == 'up':
            aim -= velocity
        elif direction == 'down':
            aim += velocity
        else: # forward
            position += velocity
            depth += aim * velocity

    print(position * depth)
