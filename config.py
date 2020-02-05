DB_URL = 'mysql://root:@localhost:3306/test?charset=utf8'
DEBUG = False

try:
    from local_settings import *   # noqa
except ImportError:
    pass  