from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

gadgets_router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi import Request

# html 틀이 있는 폴더 위치
gadgets = Jinja2Templates(directory="templates/")


@gadgets_router.get("/buttons",response_class=HTMLResponse)
async def buttons(request:Request):
    pass
    return gadgets.TemplateResponse(name="gadgets/buttons.html",context={"request":request}) # 파일상의 경로설정

# /
@gadgets_router.get("/cards") # 어노테이션(웹에서 업무(function) 호출)
# request = Request(query_parameters)
async def cards(request:Request): # 질의
    # request.query_params
    # QueryParams('name=myeongyun&email=gongmyeongyun%40gmail.com')
    # dict(request.query_params)
    # {'name': 'myeongyun', 'email': 'gongmyeongyun@gmail.com'}
    
    return gadgets.TemplateResponse(name="gadgets/cards.html",context={"request":request}) # 파일상의 경로설정

@gadgets_router.post("/cards") # 어노테이션(웹에서 업무(function) 호출)
async def cards_post(request:Request):
    # request.query_params
    # QueryParams('')
    # await request.form()
    # FormData([('name', 'myeongyun'), ('email', 'gongmyeongyun@gmail.com')])
    # dict(await request.form())
    # {'name': 'myeongyun', 'email': 'gongmyeongyun@gmail.com'}
    # form_datas = await request.form()
    # dict(form_datas)
    return gadgets.TemplateResponse(name="gadgets/cards.html",context={"request":request}) # 파일상의 경로설정

@gadgets_router.get("/colors",response_class=HTMLResponse) # 어노테이션(웹에서 업무(function) 호출)
async def colors(request:Request):
    # pass
    # return 0
    return gadgets.TemplateResponse(name="gadgets/colors.html",context={"request":request}) # 파일상의 경로설정

@gadgets_router.get("/containers",response_class=HTMLResponse) # 어노테이션(웹에서 업무(function) 호출)
async def containers(request:Request):
    # pass
    # return 0
    return gadgets.TemplateResponse(name="gadgets/containers.html",context={"request":request}) # 파일상의 경로설정