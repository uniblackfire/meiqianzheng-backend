import os

try:
    import simplejson as json
except:
    import json
from Constants import PROJECT_DIR


def read_file_content(filename):
    file_content = ''

    with open(os.path.join(PROJECT_DIR, filename), 'r', encoding='utf-8') as fd:
        for line in fd:
            file_content += line

    return json.loads(file_content)


def read_products_list_file():
    return read_file_content('data/productslist.txt')


def read_promotion_list_file():
    return read_file_content('data/SalesPromotion.txt')
