import os

try:
    import simplejson as json
except:
    import json

DEBUG_ENABLED = True  # debug enabled


def init():
    pass


def get_site_port():
    if DEBUG_ENABLED:
        return 8000
    else:
        return 80
