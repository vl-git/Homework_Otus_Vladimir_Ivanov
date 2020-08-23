from operator import pow
def powering_sequence(*args, power=2):
    print(f'Powering {args} by {power}')
    powered_sequence = map(pow, args, [power]*len(args))
    print('Got result: ')
    return list(powered_sequence)


print(', '.join(list(map(str, powering_sequence(1,2,3,4,22, 125.6, power=4)))))

