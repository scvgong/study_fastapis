from fastapi import FastAPI

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
# No 'Access-Control-Allow-Origin'
# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 환경에서는 접근 가능한 도메인만 허용하는 것이 좋습니다.
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from routes.gadgets import gadgets_router as first_router
from routes.positionings import positionings_router as second_router
from routes.homes import home_router as third_router
from routes.users import router as users_router

app.include_router(first_router,prefix='/gadgets') # 주소창의 경로 설정
app.include_router(second_router,prefix='/positionings') # 주소창의 경로 설정
app.include_router(third_router,prefix='/homes') # 주소창의 경로 설정
app.include_router(users_router,prefix='/users') # 주소창의 경로 설정

from fastapi import Request
from fastapi.templating import Jinja2Templates

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

@app.get("/") # 경로
async def root(request:Request):
    # return {"message": "Gongmyeongyun world"}
    # html 틀로 호출
    return templates.TemplateResponse("main.html",{'request':request})
