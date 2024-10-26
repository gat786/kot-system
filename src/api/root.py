from fastapi import FastAPI
from api.tables import router as tables_router
from api.menu import router as menu_router
from api.order import router as order_router

api = FastAPI()

api.include_router(tables_router)
api.include_router(menu_router)
api.include_router(order_router)

@api.get("/")
def root():
  return {"message": "Hello World"}