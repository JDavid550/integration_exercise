from typing import List
from filter_palindrome import read_file

MIT_WORDS_ROUTE = '../utils/mit_words.txt'

def look_for_words(length: int):
    words_list: List[str] = read_file(MIT_WORDS_ROUTE)
    words: List[str] = list(filter(lambda x: len(x)==length and x[0] == 'z', words_list))
    return words