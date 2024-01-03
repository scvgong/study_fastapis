from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi import Request

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

# 회원가입 / users/insert
@router.get("/inserts") # 어노테이션(웹에서 업무(function) 호출)
async def insert(request:Request):
    # pass
    # return 0
    return templates.TemplateResponse(name="users/inserts.html",context={"request":request})