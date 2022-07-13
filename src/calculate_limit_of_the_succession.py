""" This module takes the max index in dictionary and the max value of lengths.
The addition of those two numbers is the limit
of the succession of prime numbers in the next module """

from typing import Dict, Union

def calculate_limit_of_the_succession(dictionary:  Dict[int, Dict[str, Union[str, int]]]):
    """ Returns the limit of succession """
    values = dictionary.values()
    lengths = [list(i.values())[1] for i in values]
    limit = (max(list(dictionary.keys())) + max(lengths))
    return limit
