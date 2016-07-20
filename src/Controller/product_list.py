try:
    import simplejson as json
except:
    import json
from src.Controller.database import read_products_list_file, read_promotion_list_file


# 根据barcode返回该商品的具体信息
def get_product_info_by_barcode(barcode):
    items_list = read_products_list_file()
    for item_dict in items_list:
        if item_dict['barcode'] == barcode:
            return item_dict
    return None


# 根据barcode返回该商品参加的优惠活动
def get_promotions_list_type_by_barcode(barcode):
    # return a list to represent promotions!
    promotion_list = read_promotion_list_file()
    result_list = list()
    for promotion_dict in promotion_list:
        if barcode in promotion_dict['barcodes']:
            result_list.append(promotion_dict['type'])
    return result_list


# 根据促销活动的type英文名称查找中文名称
def get_promotion_name_by_type(promotion_type):
    promotion_list = read_promotion_list_file()
    for item in promotion_list:
        if promotion_type == item['type']:
            return item['name']
    return None


# 获取商品列表信息
def get_products_list(category_name=''):
    items_list = read_products_list_file()
    return_list = list()
    for item_dict in items_list:
        if len(category_name.strip()) == 0 or item_dict['categoryName'] == category_name:
            return_list.append(item_dict)
        item_dict['promotionType'] = get_promotions_list_type_by_barcode(item_dict['barcode'])
    return json.dumps(return_list)
