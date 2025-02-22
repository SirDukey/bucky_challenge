from prettytable import PrettyTable
import csv
from datetime import datetime


table = PrettyTable()
table.field_names = ['id', 'name', 'price', 'expires']


def display_table(sp):
    """
    Display product table
    """
    PRICE_MIN, PRICE_MAX, EXPIRES_START, EXPIRES_STOP = sp
    if '*' in PRICE_MIN:
        PRICE_MIN = 0
    if '*' in PRICE_MAX:
        PRICE_MAX = 999999
    if '*' in EXPIRES_START:
        EXPIRES_START = '01/01/1970'
    if '*' in EXPIRES_STOP:
        EXPIRES_STOP = '12/31/3000'
    with open('products.csv', 'r') as prod_csv:
        csv_reader = csv.DictReader(prod_csv, delimiter=',')

        start = datetime.strptime(EXPIRES_START, '%m/%d/%Y')
        start = start.strftime('%m/%d/%Y')

        stop = datetime.strptime(EXPIRES_STOP, '%m/%d/%Y')
        stop = stop.strftime('%m/%d/%Y')

        PRICE_MIN = float(PRICE_MIN)
        PRICE_MAX = float(PRICE_MAX)

        for row in csv_reader:
            price = float(row['price'])
            expires = datetime.strptime(row['expires'], '%m/%d/%Y')
            expires = expires.strftime('%m/%d/%Y')
            if price >= PRICE_MIN and price <= PRICE_MAX and expires >= start and expires <= stop:
                table.add_row([row['id'], row['name'], row['price'], row['expires']])
    print(table)
    table.clear_rows()


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
