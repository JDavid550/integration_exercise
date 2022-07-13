""" This module takes the iterator from
previous module and through a decorator
it determines the new length of words """

import math
from typing import Callable, List
import numpy as np
from primeNumbersSuccession import PrimeNumbersSuccession

def cubes(func) -> Callable:
    """A dummy docstring."""
    def wrapper(*args,**kwargs) -> int:
        listt: List[int] = func(*args, **kwargs)
        cubes_list: List[int] = [x**3 for x in listt]
        middle: int = len(cubes_list) // 2
        reduced_list: List[int] = list(
            map(
                lambda x: int(math.sqrt(x)),
                cubes_list[:middle]
        ))
        lcm: int = np.lcm.reduce(reduced_list)
        length: int = int(str(lcm)[0])
        return length
    return wrapper

@cubes
def lengths_for_new_words(nums: PrimeNumbersSuccession) -> List[int]:
    """Returns de list from the iterable"""
    return list(nums)
