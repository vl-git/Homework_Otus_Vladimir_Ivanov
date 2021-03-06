from operator import pow
from time import time
from functools import wraps
from random import randint


def time_func(func, *args, **kwargs):
    print("timing func", func.__name__, "with args", (str(args)[:-2] + ')') if args else '', kwargs if kwargs else '')
    start_time = float('%.20f'%time())
    res = func(*args, **kwargs)
    end_time = float('%.20f'%time())
    print("computed in", '%.20f'%(end_time - start_time))
    return res


def timing_dec(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return time_func(func, *args, **kwargs)

    return wrapper


@timing_dec
def powering_sequence(*args, power=2):
    print(f'Powering {args} by {power}')
    powered_sequence = list(map(pow, args, [power] * len(args)))
    print(f'Got result: {powered_sequence}')
    return powered_sequence


@timing_dec
def prime_check(n):
    if not isinstance(n, int):
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d ** 2 <= n and n % d != 0:
        d += 2
    return d ** 2 > n


@timing_dec
def filter_sequence(seq, ODD_ONLY=False, EVEN_ONLY=False, PRIMES_ONLY=False):
    if isinstance(seq, list):
        if ODD_ONLY:
            print(f'Filtering the sequence {seq} by only odd numbers')
            odd = list(filter(lambda v: v % 2 != 0 if isinstance(v, int) else False, seq))
            print(f'Got result: {odd}')
            return odd
        elif EVEN_ONLY:
            print(f'Filtering the sequence {seq} by only even numbers')
            even = list(filter(lambda v: v % 2 == 0 if isinstance(v, int) else False, seq))
            print(f'Got result: {even}')
            return even
        elif PRIMES_ONLY:
            print(f'Filtering the sequence {seq} by only prime numbers')
            primes = list(filter(prime_check, seq))
            print(f'Got result: {primes}')
            return primes
        else:
            print('You should choose one of the filter options')
            return None
    else:
        print('The sequence should be list type')
        return None


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__, (str(args)[:-2] + ')') if args else '', kwargs if kwargs else '')
        return func(*args, **kwargs)

    return wrapper


@trace
def fib_numbers(q, prev=1, curr=1, flag=True):
    if flag:
        print(f'First {q} Fibonacci numbers:')
    print(prev, end=' ')
    curr += prev
    prev = curr - prev
    q -= 1
    if q == 0:
        return None
    fib_numbers(q, prev=prev, curr=curr, flag=False)


powering_sequence(1, 2, 3, 4, 22, 125.6, power=4)
print()
test_seq1 = [randint(0, 1000) for i in range(0,25)]
test_seq2 = (1, 2, 3, 4, 5, 7, 9, 10, 17, 225, 15.6)
filter_sequence(test_seq2, ODD_ONLY=True)
print()
filter_sequence(test_seq1)
print()
filter_sequence(test_seq1, PRIMES_ONLY=True)
print()
fib_numbers(20)
