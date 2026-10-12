
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(req: Request):
    say_hi = "Hello, welcome to my cafe!"

    return templates.TemplateResponse(
        request=req,
        name="home.html",
        context={"say_hi": say_hi}
    )


@app.get("/products", response_class=HTMLResponse)
def products(req: Request):
    products = [
        (1, "Laptop", 70000),
        (2, "iPhone", 80000)
    ]

    return templates.TemplateResponse(
        request=req,
        name="product.html",
        context={"products": products}
        
    )
# @app.post("/login")
# def login(username:str=Form(),password:str=Form()):
#     print(username,password)
#     return templates.TemplateResponse(
#         request=username,
#         name="product.html"
#         context={}
#     )