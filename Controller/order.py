import collections
import re

from Controller.Promotion import Promotion
from Controller.product_list import get_promotions_list_type_by_barcode, get_product_info_by_barcode, \
    get_promotion_name_by_type

# 分隔符
LINE_BREAK = '----------------------\n'


def order_process(post_data):
    customer_item_dict = get_items_dict(post_data)

    # 输出小票
    # 基本的购物统计信息
    basic_info = ''

    # 最后的总价格
    total_price = 0
    # 总共节省的金额
    total_save = 0
    # 促销信息
    promotion_msg_dict = dict()
    for barcode, number in customer_item_dict.items():
        # barcode表示每个商品的barcode
        # number表示每个商品的个数

        # 单价
        unit_price = get_product_info_by_barcode(barcode)['price']
        # 商品名称
        product_name = get_product_info_by_barcode(barcode)['name']
        # 计量单位名称
        unit_name = get_product_info_by_barcode(barcode)['unit']
        # 每种商品优惠前的总价
        items_price = unit_price * number
        promotion_list = get_promotions_list_type_by_barcode(barcode)
        new_price_list = list()

        if promotion_list:
            for promotion in promotion_list:
                # 反射调用对应于promotion['type']的促销逻辑类
                promotion_instance = Promotion.get_promotion_class(
                    promotion,
                    product_name,
                    items_price,
                    number,
                    unit_price,
                    unit_name)
                new_items_price = promotion_instance.get_new_items_price()
                new_price_list.append(new_items_price)

            cheapest_promotion = promotion_list[new_price_list.index(min(new_price_list))]
            promotion_instance = Promotion.get_promotion_class(
                cheapest_promotion,
                product_name,
                items_price,
                number,
                unit_price,
                unit_name)
            # 促销活动名称
            promotion_name = get_promotion_name_by_type(cheapest_promotion)

            # 每种参加优惠活动的商品的信息
            promot_msg = promotion_instance.get_promote_message()

            if promot_msg:
                if promotion_name not in promotion_msg_dict.keys():
                    promotion_msg_dict.setdefault(promotion_name, '')

                promotion_msg_dict[promotion_name] += promot_msg

            tmp_items_price = items_price
            # 每种商品优惠后的总价
            items_price = promotion_instance.get_new_items_price()
            # 累计总共优惠的金额
            total_save += tmp_items_price - items_price
            basic_info += promotion_instance.get_basic_info()
        else:
            basic_info += '名称：%s，数量：%d%s，单价：%.2f(元)，小计：%.2f(元)\n' \
                          % (product_name, number, unit_name, unit_price, items_price)
        total_price += items_price

    output_message = '***<没钱赚商店>购物清单***\n'
    output_message += '%s' % basic_info
    output_message += LINE_BREAK
    if promotion_msg_dict:
        for k, v in promotion_msg_dict.items():
            output_message += k + '：\n'  # get_promotion_name_by_type(promotion)
            output_message += v
            output_message += LINE_BREAK
            output_message += '总计：%.2f(元)\n' % total_price
    if total_save:
        output_message += '节省：%.2f(元)\n' % total_save
    output_message += '**********************\n'
    # 返回小票信息
    return output_message


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
