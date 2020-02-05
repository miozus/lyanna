from sanic import Blueprint

from ext import mako
from models import Post

bp = Blueprint('views') # 注册蓝图


@bp.route('/')  # 路由：根目录
@mako.template('index.html') # 装饰器，async def 之上
async def index(request):
    name = request.args.get('title', 'World') # 拿参数，如果没有默认为World
    post = await Post.create(title=name)
    print(await Post.filter(title=name).first())
    return {'post': post}  # 返回的结果给template使用