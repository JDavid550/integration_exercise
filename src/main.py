from filterPalindrome import filterPalindrome
from generateDictionaries import generateDictionaries
from calculateLimitOfTheSuccession import calculateLimitOfTheSuccession

def run():
    palindromes = filterPalindrome()
    dictionary = generateDictionaries(palindromes)
    calculateLimitOfTheSuccession(dictionary)


if __name__ == '__main__':
    run()