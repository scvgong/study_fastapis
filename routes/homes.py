from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

home_router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi import Request

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

# /home
# @router.get("/",response_class=HTMLResponse) # 경로
# async def home():
#     # return {"message": "home world"}
#     html = "<body> <h2>It's Home</h2> </body>"
#     return html

@home_router.get("/standards")
async def root(request:Request):
    pass
    return templates.TemplateResponse(name="homes/standards.html",context={"request":request})

# /home/list
@home_router.get("/list",response_class=HTMLResponse) # 어노테이션(웹에서 업무(function) 호출)
async def home_list():
    # pass
    # return 0
    html = "<body> <h2>It's Home list</h2> </body>"
    return html

# /homes/params_query -> parameters_query.html 호출
@home_router.get("/params_query")
async def home(request:Request):
    pass
    return templates.TemplateResponse(name="homes/parameters_query.html",context={"request":request})