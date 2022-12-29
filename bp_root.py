from sanic import Sanic, Blueprint
from sanic.response import text,json
import sanic

bp = Blueprint("my_blueprint")


@bp.route("/")
async def bp_root(request):
    return json({"my": "blueprint"})