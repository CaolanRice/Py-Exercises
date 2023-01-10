# if len of people = 4, i starts at index 0 and j should start at index 1 and iterate
def printHandshakes(people):
    numberOfHandshakes = 0
    for i in range(0, len(people) - 1):
        for j in range(i + 1, len(people)):
            print(f'{people[i]} shakes hands with {people[j]}')
            numberOfHandshakes += 1
    print(f'The total number of handshakes was -> {numberOfHandshakes}')
    return numberOfHandshakes


assert printHandshakes(['Alice', 'Bob']) == 1
assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3
assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6
