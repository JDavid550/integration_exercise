FINAL_ROUTE = '../utils/final.txt'



def write(list):
    with open(FINAL_ROUTE,'a+', encoding='utf-8') as f:
        for i in list:
            f.write(f'{i} \n')