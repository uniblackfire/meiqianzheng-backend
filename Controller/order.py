import collections
import re

from Controller.product_list import get_promotion_type_by_barcode


def order_process(post_data):
    customer_item_dict = get_items_dict(post_data)
    # Promotion.get_promotion_class('BUY_TWO_GET_ONE_FREE', '', '', 1, '', '')

    for barcode, number in customer_item_dict.items():
        # barcode表示每个商品的barcode
        # number表示每个商品的个数
        # 单价
        unit_price = get_promotion_type_by_barcode(barcode)['price']
        # 商品名称
        product_name = get_promotion_type_by_barcode(barcode)['name']
        # 计量单位名称
        unit_name = get_promotion_type_by_barcode(barcode)['unit']
        # 每种商品优惠前的总价
        items_price = unit_price * number

    # 返回小票信息
    return 'ok'


def get_items_dict(items_string):
    '''
    处理购物信息,并转化为字典形式
    :param items_string: 从对话框读取到的商品列表信息
    :return: 返回商品列表的字典
    '''

    def default_factory():
        return 0

    items_dict = collections.defaultdict(default_factory)

    pattern = re.compile(r"(?<=\')ITEM\d+(?=\')", re.IGNORECASE)
    items_list = re.findall(pattern, items_string)
    for item in items_list:
        items_dict[item] += 1

    pattern = re.compile(r"(?<=\')ITEM\d+-\d(?=\')", re.IGNORECASE)
    multi_items = re.findall(pattern, items_string)
    for item in multi_items:
        item_splited = item.split('-')
        for i in range(int(item_splited[1])):
            items_dict[item_splited[0]] += 1

    return dict(items_dict)
