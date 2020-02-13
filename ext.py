from tortoise import Tortoise
from sanic_mako import SanicMako

from config import DB_URL

# E1: dwm定制版的sanic_mako: https://github.com/dongweiming/sanic-mako.git
# E2: .gitignore 忽略本地下载文件（网络共享资源）

mako = SanicMako()

async def init_db(create_db=False):
    await Tortoise.init(
        db_url=DB_URL,
        modules={'models': ['models']},
        _create_db=create_db
    )