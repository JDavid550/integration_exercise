from ast import Try


def generator(list):
    n = 1
    try:
        for i in list:
            yield [n,i]
            n += 1
    except:
        print('No more words')
    