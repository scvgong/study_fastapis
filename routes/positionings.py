from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

positionings_router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi import Request

# html 틀이 있는 폴더 위치
positionings = Jinja2Templates(directory="templates/")


@positionings_router.get("/forms",response_class=HTMLResponse)
async def buttons(request:Request):
    pass
    return positionings.TemplateResponse(name="positionings/forms.html",context={"request":request})

# /
@positionings_router.get("/grids",response_class=HTMLResponse) # 어노테이션(웹에서 업무(function) 호출)
async def cards(request:Request):
    # pass
    # return 0
    return positionings.TemplateResponse(name="positionings/grids.html",context={"request":request})

@positionings_router.get("/standards",response_class=HTMLResponse) # 어노테이션(웹에서 업무(function) 호출)
async def cards(request:Request):
    # pass
    # return 0
    return positionings.TemplateResponse(name="positionings/standards.html",context={"request":request})

@positionings_router.get("/tables",response_class=HTMLResponse) # 어노테이션(웹에서 업무(function) 호출)
async def cards(request:Request):
    # pass
    # return 0
    return positionings.TemplateResponse(name="positionings/tables.html",context={"request":request})