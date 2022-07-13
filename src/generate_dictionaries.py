""" This module generates a dictionary with sub-dictionaries with the words and the lengths """

from typing import Union, Dict, List

StrOrInt = Union[str,int]

def generate_dictionaries(list_of_palindromes: List[str]) -> Dict[int, Dict[str, StrOrInt]]:
    """ Takes palindromes and generates a dictionry """
    dictionary: Dict[int ,Dict[str, StrOrInt]] = {
        list_of_palindromes.index(i) : {
            'word':i,
            'length': len(i)
        } for i in list_of_palindromes}
    return dictionary
