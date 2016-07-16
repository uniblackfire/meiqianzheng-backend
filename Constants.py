import os
DEBUG_ENABLED = True  # debug enabled


def init():
    pass


def get_site_port():
    if DEBUG_ENABLED:
        return 8000
    else:
        return 80


project_dir = os.path.dirname(os.path.abspath(__file__))
