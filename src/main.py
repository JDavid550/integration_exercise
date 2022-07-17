import imp
from filter_palindrome import filter_palindrome
from generate_dictionaries import generate_dictionaries
from calculate_limit_of_the_succession import calculate_limit_of_the_succession
from look_for_words import look_for_words
from primeNumbersSuccession import PrimeNumbersSuccession
from lengths_for_new_words import lengths_for_new_words
from generator import generator
from closure import closure
from write import write

#Access point
def run():
    """ Runs the functions imported in order """
    palindromes = filter_palindrome()
    dictionary = generate_dictionaries(palindromes)
    limit_succession = calculate_limit_of_the_succession(dictionary)
    primes = PrimeNumbersSuccession(limit_succession)
    length = lengths_for_new_words(primes)
    new_words = look_for_words(length)
    gen = generator(new_words)
    final_words = []
    for i in gen:
        final_words.append(i)
    init_closure = closure(final_words)
    list_multiplied = init_closure(2)
    write(list_multiplied)



if __name__ == '__main__':
    run()
    