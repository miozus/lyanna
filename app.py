from sanic import Sanic

from ext import mako, init_db
from config import DEBUG

from views import bp

app = Sanic(__name__)
mako.init_app(app) # 延迟执行
app.blueprint(bp)
app.static('/static', './static') # 静态方式设置子路径

@app.listener('before_server_start') # 启动器
async def setup_ab(app, loop):
    await init_db() # 全局初始化一次，都可以用了


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=0000, debug=DEBUG)    