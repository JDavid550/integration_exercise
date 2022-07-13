""" This module filte the palindromes from the list of words """

from typing import List

def read_file() -> List[str]:
    """ Reads file """
    data: List[str] = []
    with open('../utils/randomWords.txt', 'r', encoding='utf-8') as f:
        for i in f:
            data.append(i.rstrip('\n').lower().replace(" ", ""))
    return data


def filter_palindrome() -> List[str]:
    """ Filer palindrome words """
    words: List[str] = read_file()
    palindromes = list(filter(lambda word: word == word[::-1], words))
    return palindromes