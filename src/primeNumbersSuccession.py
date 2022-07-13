""" This module contains the iterator for prime numbers succession """
from typing import  List


class PrimeNumbersSuccession:
    """Iterable to return a succession of prime numbers"""
    def __init__(self, limit):
        self.max = limit
        self.primes: List[int] = []
        self.n_1: int = 1
        self.n_2: int = self.n_1 + 1

    def __iter__(self):
        return self

    def __next__(self) -> int:
        while True:
            is_prime = True
            for prime in self.primes:
                if self.n_2 % prime == 0:
                    is_prime = False
                    break

            if is_prime:
                self.primes.append(self.n_2)
                self.n_1 = self.n_2
                if self.n_1 > self.max:
                    raise StopIteration
                break
            else:
                self.n_2 += 1

        return self.n_1