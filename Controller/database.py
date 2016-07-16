import os
from Constants import project_dir


def read_products_list_file():
    file_content = ''

    with open(os.path.join(project_dir, 'productslist.txt'), 'r', encoding='utf-8') as fd:
        for line in fd:
            file_content += line

    return file_content
