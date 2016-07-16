try:
    import simplejson as json
except:
    import json

from Controller.database import read_products_list_file


def get_promotion_type_by_barcode(barcode):
    # return a list to represent promotions!
    return ['man3mian1', 'ceshiceshi']


# json.dumps(items_list)
def get_products_list(category_name=''):
    data = read_products_list_file()
    items_list = json.loads(data)
    return_list = list()
    for item_dict in items_list:
        if len(category_name.strip()) == 0 or item_dict['categoryName'] == category_name:
            return_list.append(item_dict)
        item_dict['promotionType'] = get_promotion_type_by_barcode(item_dict['barcode'])
    return json.dumps(return_list)
