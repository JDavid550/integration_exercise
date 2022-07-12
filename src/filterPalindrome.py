from typing import List


def readFile() -> List[str]:
    data: List[str] = []
    with open('../utils/randomWords.txt', 'r', encoding='utf-8') as f:
        for i in f:
            data.append(i.rstrip('\n').lower().replace(" ", ""))
    return data


def filterPalindrome() -> List[str]:
    words: List[str] = readFile()
    palindromes = list(filter(lambda word: word == word[::-1], words))
    return palindromes