from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi import Request

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

# 회원가입 form /users/form -> users/inserts.html
@router.get("/form") 
async def form(request:Request):
    return templates.TemplateResponse(name="users/inserts.html",context={"request":request})

# 회원가입(post 방식) /users/insert -> users/logins.html
@router.post("/inserts")
async def insert(request:Request):
    dict_details = dict(await request.form())
    print(dict_details)
    pass # business
    return templates.TemplateResponse(name="users/logins.html",context={"request":request})

# 회원리스트(post 방식) /users/login -> users/lists.html
@router.post("/lists") 
async def list(request:Request):
    dict_details = dict(await request.form())
    print(dict_details)
    pass # business
    return templates.TemplateResponse(name="users/lists.html",context={"request":request})

# 회원리스트(get 방식) /users/lists -> users/lists.html
@router.get("/lists")
async def list(request:Request):
    dict_details = dict(await request.form())
    print(dict_details)
    pass # business
    return templates.TemplateResponse(name="users/lists.html",context={"request":request})

# 회원상세정보 /users/reads -> users/reads.html
# Path parameters : /users/reads/id or /users/reads/uniqe_name
@router.get("/reads/{object_id}") 
async def read(request:Request,object_id):
    dict_details = dict(await request.form())
    print(dict_details)
    pass # business
    return templates.TemplateResponse(name="users/reads.html",context={"request":request})

#회원가입(post) -> 로그인(post) -> 회원리스트(get) -> 회원 상세 : 리스트(get), 삭제(post)