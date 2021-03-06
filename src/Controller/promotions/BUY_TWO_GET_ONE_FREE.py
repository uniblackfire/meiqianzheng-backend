from src.Controller.Promotion import Promotion


class BUY_TWO_GET_ONE_FREE(Promotion):
    def __init__(self,
                 product_name,
                 original_price,
                 items_num,
                 unit_price,
                 unit_name):
        '''
        买三免一的优惠活动的逻辑
        :param product_name: 商品名称
        :param original_price: 优惠前该种商品的总价
        :param items_num: 该商品的个数
        :param unit_price: 商品单价
        :param unit_name: 计量单位
        :return:
        '''
        super().__init__()
        self.items_num = items_num
        self.free_num = self.items_num // 3
        self.unit_price = unit_price
        self.price = original_price
        self.new_price = original_price
        self.product_name = product_name
        self.unit_name = unit_name

    def get_new_items_price(self):
        '''

        :return: 返回该种商品的新的总价
        '''
        super().get_new_items_price()
        save_price = self.free_num * self.unit_price
        self.new_price -= save_price
        return self.new_price

    def get_promote_message(self):
        '''

        :return: 生成优惠信息,准备输出到小票上
        '''
        super().get_promote_message()
        if self.free_num == 0:
            return None
        return '名称：%s，数量：%d%s\n' % (self.product_name, self.free_num, self.unit_name)

    def get_basic_info(self):
        return '名称：%s，数量：%d%s，单价：%.2f(元)，小计：%.2f(元)\n' \
               % (self.product_name,
                  self.items_num,
                  self.unit_name,
                  self.unit_price,
                  self.new_price)
