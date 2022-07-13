from filter_palindrome import filter_palindrome
from generate_dictionaries import generate_dictionaries
from calculate_limit_of_the_succession import calculate_limit_of_the_succession
from primeNumbersSuccession import PrimeNumbersSuccession
from lengths_for_new_words import lengths_for_new_words

#Access point
def run():
    """ Runs the functions imported in order """
    palindromes = filter_palindrome()
    dictionary = generate_dictionaries(palindromes)
    limit_succession = calculate_limit_of_the_succession(dictionary)
    primes = PrimeNumbersSuccession(limit_succession)
    length = lengths_for_new_words(primes)
    print(length)


if __name__ == '__main__':
    run()
    