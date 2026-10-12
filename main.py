
# from fastapi import FastAPI, Request
# from fastapi.templating import Jinja2Templates
# from fastapi.responses import HTMLResponse

# app = FastAPI()

# templates = Jinja2Templates(directory="templates")


# @app.get("/", response_class=HTMLResponse)
# def home(req: Request):
#     say_hi = "Hello, welcome to my cafe!"

#     return templates.TemplateResponse(
#         request=req,
#         name="home.html",
#         context={"say_hi": say_hi}
#     )


# @app.get("/products", response_class=HTMLResponse)
# def products(req: Request):
#     products = [
#         (1, "Laptop", 70000),
#         (2, "iPhone", 80000)
#     ]

#     return templates.TemplateResponse(
#         request=req,
#         name="product.html",
#         context={"products": products}
        
#     )



from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from database import get_connection

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
    connection = None
    cursor = None

    try:
        # Connect to MySQL
        connection = get_connection()

        # Create cursor
        cursor = connection.cursor()

        # Fetch products from MySQL
        cursor.execute("SELECT * FROM products")

        # Get all product records
        products = cursor.fetchall()

        # Send records to HTML template
        return templates.TemplateResponse(
            request=req,
            name="product.html",
            context={"products": products}
        )

    finally:
        # Close cursor and connection
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()
