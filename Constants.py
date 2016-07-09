import os

try:
    import simplejson as json
except:
    import json

DEBUG_ENABLED = True  # debug enabled
CONFIG_FILE_NAME = 'config.json'
# default website info, must configured by yourself!
CONFIG = {
    'DATABASE': {
        'host': '192.168.1.125',
        'port': 27017,
        'name': 'findgf',
        'username': 'dbadmin',
        'password': 'password',
    },

    'WEBSITE': {
        'name': '我的简历',
        'domain': 'mianshi100.com',
        'keywords': ['找工作', '面试', '求职', 'hr', 'offer'],
        'description': 'this is description!',
        'author': 'blackman',
        'autograph': '这是我的签名!~<br/>哼哼!',
        'portrait_url': './static/images/avatar.jpg',
    }
}

# page settings
RESULTS_PER_PAGE = 10
CURRENT_MONGODB = None


def init_config():
    global CONFIG

    CONFIG['WEBSITE']['url'] = 'http://www.' + CONFIG['WEBSITE']['domain']
    CONFIG['WEBSITE']['copyright_info'] = '&copy; ' + CONFIG['WEBSITE']['domain'] + '. All rights reserved.'
    with open(CONFIG_FILE_NAME, 'w') as f:
        f.write(json.dumps(CONFIG, indent=' ' * 4))


def read_config():
    global CONFIG_FILE_NAME
    global CONFIG
    CONFIG_FILE_NAME = os.path.join(os.path.dirname(__file__), CONFIG_FILE_NAME)
    if not os.path.isfile(CONFIG_FILE_NAME) or os.stat(CONFIG_FILE_NAME).st_size == 0:
        init_config()
    else:  # read in config file
        with open(CONFIG_FILE_NAME, 'r') as fd:
            CONFIG = json.loads(fd.read())


def init():
    '''注释
    init website
    :return:
    '''
    global CURRENT_MONGODB
    read_config()
    # CURRENT_MONGODB = DBUtils.get_mongodb(CONFIG['DATABASE']['host'],
    #                                       CONFIG['DATABASE']['port'],
    #                                       CONFIG['DATABASE']['name'],
    #                                       CONFIG['DATABASE']['username'],
    #                                       CONFIG['DATABASE']['password'])


def get_site_port():
    if DEBUG_ENABLED:
        return 8000
    else:
        return 80


def get_root_url():
    if DEBUG_ENABLED:
        return 'http://localhost:' + str(get_site_port())
    else:
        return CONFIG['WEBSITE']['url']
