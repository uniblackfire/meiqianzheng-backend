# -*- coding: UTF-8 -*-


class Promotion:
    def __init__(self):
        pass

    def get_new_items_price(self):
        pass

    def get_promote_message(self):
        pass

    def get_basic_info(self):
        pass

    @staticmethod
    def get_promotion_class(promotion_type,
                            product_name,
                            original_price,
                            items_num,
                            unit_price,
                            unit_name):
        '''
        根据优惠类型,决定实例化哪一个子类
        :param promotion_type:
        :param product_name:
        :param original_price:
        :param items_num:
        :param unit_price:
        :param unit_name:
        :return:
        '''
        # 根据 promotion_type 去找对应文件名的py文件
        _packet_name = 'src.Controller.promotions.' + promotion_type
        promotion_module = __import__(_packet_name, fromlist=True)
        obj = getattr(promotion_module, promotion_type)
        return obj(
            product_name,
            original_price,
            items_num,
            unit_price,
            unit_name
        )


'''
    @staticmethod
    def get_all_promotion_class():
        path = os.path.abspath(os.path.join(Constants.PROJECT_DIR, 'Controller', 'promotions'))
        files = os.listdir(path)
        py_file_re = re.compile('\.py$', re.IGNORECASE)
        files = filter(py_file_re.search, files)
        print(files)
        file_name_to_module_name = lambda f:os.path.splitext(f)[0]
        modulesNames = map(file_name_to_module_name, files)
        print(modulesNames)
        modules = list(map(__import__, modulesNames))
        for mod in modules:
            obj = getattr(mod, 'BUY_TWO_GET_ONE_FREE')
            print(obj)
        return modules
'''
