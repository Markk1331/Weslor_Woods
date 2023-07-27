def print_formatted(number):
    width = 6
    for x in range(1,int(number)+1):
        shift = number.bit_length()
        print(f'{x:{shift}d} {x:{shift}o} {x:{shift}X} {x:{shift}b}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)