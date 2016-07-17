import collections
import json
import re


def order_process(post_data):
    items_dict = get_items_dict(post_data)
    print(items_dict)
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
