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
    return gadgets.TemplateResponse(name="gadgets/buttons.html",context={"request":request})

# /
@gadgets_router.get("/cards",response_class=HTMLResponse) # 어노테이션(웹에서 업무(function) 호출)
async def cards(request:Request):
    # pass
    # return 0
    return gadgets.TemplateResponse(name="gadgets/cards.html",context={"request":request})

@gadgets_router.get("/colors",response_class=HTMLResponse) # 어노테이션(웹에서 업무(function) 호출)
async def colors(request:Request):
    # pass
    # return 0
    return gadgets.TemplateResponse(name="gadgets/colors.html",context={"request":request})

@gadgets_router.get("/containers",response_class=HTMLResponse) # 어노테이션(웹에서 업무(function) 호출)
async def containers(request:Request):
    # pass
    # return 0
    return gadgets.TemplateResponse(name="gadgets/containers.html",context={"request":request})