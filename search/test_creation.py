from random import randint

NUM_SPACES = 7 * 7


def create_test():
    f = open('ctest.csv', 'w')

    used_coordinates = set()
    num_reds = int(input("Enter number of red pieces: "))
    num_blues = int(input("Enter number of blue pieces: "))

    if num_blues + num_reds > NUM_SPACES:
        raise Exception("Too many pieces")

    for i in range(num_reds):
        while (coord := (randint(0, 6), randint(0, 6))) in used_coordinates:
            pass
        used_coordinates.add(coord)
        state = list(coord) + ['r', randint(1, 6)]
        print(state)
        f.write(', '.join([str(x) for x in state]) + '\n')

    for i in range(num_blues):
        while (coord := (randint(0, 6), randint(0, 6))) in used_coordinates:
            pass
        used_coordinates.add(coord)
        state = list(coord) + ['b', randint(1, 6)]
        print(state)
        f.write(', '.join([str(x) for x in state]) + '\n')

    f.close()
