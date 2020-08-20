def powering_sequence(*args, power=2):
    print(f'Powering {args} by {power}')
    powered_sequence = map(lambda num: num**power if isinstance(num, (int, float)) else 'INCORRECT VALUE', args)
    print('Got result: ')
    return list(powered_sequence)


print(', '.join(list(map(str, powering_sequence(1,2,3,4,22,'d', 125.6, power=4)))))

