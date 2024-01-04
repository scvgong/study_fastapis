from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi import Request

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

# 회원가입 form /users/form -> users/inserts.html
@router.get("/form") # 어노테이션(웹에서 업무(function) 호출)
async def insert(request:Request):
    return templates.TemplateResponse(name="users/inserts.html",context={"request":request})

# 회원가입 /users/insert -> users/logins.html
@router.get("/inserts") # 어노테이션(웹에서 업무(function) 호출)
async def insert(request:Request):
    pass # business
    return templates.TemplateResponse(name="users/logins.html",context={"request":request})

# 회원리스트 /users/lists -> users/lists.html
@router.get("/lists") # 어노테이션(웹에서 업무(function) 호출)
async def list(request:Request):
    pass # business
    return templates.TemplateResponse(name="users/lists.html",context={"request":request})

# 회원상세정보 /users/reads -> users/reads.html
# Path parameters : /users/reads/id or /users/reads/uniqe_name
@router.get("/reads/{object_id}") 
async def list(request:Request,object_id):
    pass # business
    return templates.TemplateResponse(name="users/reads.html",context={"request":request})