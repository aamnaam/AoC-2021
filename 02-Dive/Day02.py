def move_sub(statement, initial_pos):
    direction = statement[0]
    amt = int(statement[1])

    if direction == "forward":
        initial_pos[0] += amt
    elif direction == "down":
        initial_pos[1] += amt
    else:
        initial_pos[1] -= amt


def alt_move_sub(statement, initial_pos):
    direction = statement[0]
    amt = int(statement[1])

    if direction == "forward":
        initial_pos[0] += amt
        initial_pos[1] += initial_pos[2] * amt

    elif direction == "down":
        initial_pos[2] += amt
    else:
        initial_pos[2] -= amt


def main():
    with open("input.txt") as f:
        moves = [line.split(" ") for line in f.read().split("\n")]
    pos = [0, 0]
    alt_pos = [0, 0, 0]

    for move in moves:
        move_sub(move, pos)
        alt_move_sub(move, alt_pos)

    print(f"Part 1: {pos[0] * pos[1]}")
    print(f"Part 2: {alt_pos[0] * alt_pos[1]}")


if __name__ == '__main__':
    main()
