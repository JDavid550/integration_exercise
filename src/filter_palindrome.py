""" This module filte the palindromes from the list of words """

from typing import List

ROUTE_RANDOM_WORDS = '../utils/randomWords.txt' 

def read_file(file_route:str) -> List[str]:
    """ Reads file """
    data: List[str] = []
    with open(file_route, 'r', encoding='utf-8') as f:
        for i in f:
            data.append(i.rstrip('\n').lower().replace(" ", ""))
    return data


def filter_palindrome() -> List[str]:
    """ Filer palindrome words """
    words: List[str] = read_file(ROUTE_RANDOM_WORDS)
    palindromes = list(filter(lambda word: word == word[::-1], words))
    return palindromes