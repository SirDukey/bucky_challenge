from prettytable import PrettyTable, from_csv

table = PrettyTable()
table.field_names = ['id', 'name', 'price', 'expires']


def display_table(sp):
    
    """
    Display product table
    """
    """
    table.add_row([1, 'First sample item', 1.23, 'JAN-01-2019'])
    table.add_row([2, 'Second sample item', 2.34, 'JAN-02-2019'])
    print(table)
    table.clear_rows()
    """

    with open('products.csv', 'r') as f:
        prod_table = from_csv(f)

    PRICE_MIN, PRICE_MAX, EXPIRES_START, EXPIRES_STOP = sp
    t = prod_table.get_string(header=False, border=False, start=0, end=10)
    print(t) 

def start():
    """
    Start accepting user input
    Quit program when user types 'exit'
    """

    while True:
        value = input('> ')
        if value == 'exit':
            break
        else:
            values = value.split(' ')
            if len(values) != 4:
                print('Supply only 4 values or type exit')
            else:
                PRICE_MIN = values[0]
                PRICE_MAX = values[1]
                EXPIRES_START = values[2]
                EXPIRES_STOP = values[3]
                search_params = (PRICE_MIN, PRICE_MAX, EXPIRES_START, EXPIRES_STOP)
                display_table(search_params)


if __name__ == '__main__':
    start()
