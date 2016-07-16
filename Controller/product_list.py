try:
    import simplejson as json
except:
    import json

from Controller.database import read_products_list_file


def get_promotion_type_by_barcode(barcode):
    return ''


def add_promotion_type_to_products_list():
    data = read_products_list_file()
    items_list = json.loads(data)

    return data
