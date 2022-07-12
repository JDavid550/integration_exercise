from typing import Union, Dict, List

strOrInt = Union[str,int]


def generateDictionaries(listOfPalindromes: List[str]) -> Dict[int, Dict[str, strOrInt]]:
    dictionary: Dict[int ,Dict[str, strOrInt]] = {
        listOfPalindromes.index(i) : {
            'word':i, 
            'length': len(i)
        } for i in listOfPalindromes}
    return dictionary