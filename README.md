# FastApi

* framework, high performance, easy to learn, fast to code, ready for production
* offical : https://fastapi.tiangolo.com/

```
~$ vi main.py
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}
~$ uvicorn main:app --reload
@http://127.0.0.1:8000/
@http://127.0.0.1:8000/docs
@http://127.0.0.1:8000/redoc
```

## Main Functions
### Beginner Function
| 분류 | 설명 | 비고 |
| --- | --- | --- |
| Parameters | [Path](https://fastapi.tiangolo.com/tutorial/path-params/), [Query](https://fastapi.tiangolo.com/tutorial/query-params/) |  |
| Return Type | [Response](https://fastapi.tiangolo.com/tutorial/response-model/), [Extra](https://fastapi.tiangolo.com/tutorial/extra-models/) |  |
| etc | [Static Files](https://fastapi.tiangolo.com/tutorial/static-files/), [CORS](https://fastapi.tiangolo.com/tutorial/cors/) | -- |

### Intermediate Function
| 분류 | 설명 | 비고 |
| --- | --- | --- |
| Request | [body-Pydantic](https://fastapi.tiangolo.com/tutorial/body/), [Multiple](https://fastapi.tiangolo.com/tutorial/body-multiple-params/), [Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/), [Form Data](https://fastapi.tiangolo.com/tutorial/request-forms/) |  |
| Validations | [Path](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/), [Query](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/) |  |

### Advanced Function
| 분류 | 설명 | 비고 |
| --- | --- | --- |
| Parameters | [Cookie](https://fastapi.tiangolo.com/tutorial/cookie-params/), [Header](https://fastapi.tiangolo.com/tutorial/header-params/) |  |
| [Security](https://fastapi.tiangolo.com/tutorial/security/) | [First Steps](https://fastapi.tiangolo.com/tutorial/security/first-steps/), [Simple OAuth2](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/), [Bearer with JWT](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/) |  |

### install command

~$ pip install fastapi jinja2 <br>
~$ pip install fastapi uvicon <br>
~$ pip install python-multipart


회원가입(post) -> 로그인(post) -> 회원리스트(get) -> 회원 상세 : 리스트(get), 삭제(post)
function 내에 print : query or path parameters
