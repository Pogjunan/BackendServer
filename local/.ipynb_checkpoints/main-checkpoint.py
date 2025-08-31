# main.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 홈 메뉴 페이지: 로그인 페이지로 이동할 수 있는 링크를 제공
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})

# 로그인 폼 페이지
@app.get("/login", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", context={"request": request})

# 로그인 폼 제출 처리
@app.post("/login", response_class=HTMLResponse)
async def login_submit(request: Request, username: str = Form(...), password: str = Form(...)):
    # 예시를 위한 하드코딩된 인증 처리 (실제로는 DB 검증 등 수행)
    if username == "admin" and password == "1234":
        # 로그인 성공 -> 성공 페이지로 이동
        return templates.TemplateResponse("success.html", context={"request": request, "user": username})
    else:
        # 로그인 실패 -> 오류 메시지를 담아 다시 로그인 폼 렌더링
        return templates.TemplateResponse("login.html", context={"request": request, "error": "Invalid credentials"})
