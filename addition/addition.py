#!/usr/bin/env python3

def successor(x: int) -> int:
    '''Return the next integer.'''
    return x + 1

def predecessor(x: int) -> int:
    '''Return the previous integer.'''
    return x - 1

def sum(a, b: int) -> int:
    '''Return the sum of given positive integers using recursion.'''
    if a < 0 or b < 0:
        print('\n\t' + 'Enter two positive integers!' + '\n')
        a = int(input('\t\t> '))
        b = int(input('\t\t> '))
        return sum(a, b)
    return a if b == 0 else successor(sum(a, predecessor(b)))

def start():
    print('\n\t' + 'Enter two non-negative integers you want to sum:' + '\n')
    main()

def main():
    try:
        a = int(input('\t\t> '))
        b = int(input('\t\t> '))
    except:
        print('\n\t' + 'Enter integers!' + '\n')
        return main()
    print('\n\t' + 'RESULT: ', sum(a, b), '\n')

if __name__ == '__main__':
    start()
