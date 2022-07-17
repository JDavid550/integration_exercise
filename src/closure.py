from typing import final

def closure(list):
    
    def multiply_words(n):
        multiples = [x[0]*n for x in list]
        words_to_print=[]
        for k in list:
            for j in multiples:
                words_to_print.append(k[1]*j)
        return words_to_print

    return multiply_words




