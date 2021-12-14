
from pathlib import Path

INPUT_FILE = 'input.txt'

filePath = Path(__file__).with_name(INPUT_FILE)
with filePath.open('r') as input:
    lines = input.readlines()

    position = 0
    depth = 0

    for line in lines:
        command = line.split()
        direction = command[0]
        velocity = int(command[1])

        if direction == 'up':
            depth -= velocity
        elif direction == 'down':
            depth += velocity
        else: # forward
            position += velocity

    print(position * depth)
