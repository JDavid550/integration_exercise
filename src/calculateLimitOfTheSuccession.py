from typing import Dict, Union

def calculateLimitOfTheSuccession(dictionary: Dict[int ,Dict[str, Union[str, int]]]):
    values = dictionary.values()
    lengths = [list(i.values())[1] for i in values]
    limit = max(dictionary.keys()) + max(lengths)
    print(limit)


