from fastapi import APIRouter

router = APIRouter(
  prefix="/tables"
)

@router.get("/")
def get_tables():
  """
  This will return all the tables
  This will give you information regarding what is the current
  status of table i.e. whether it is reserved or not.
  """
  return {"message": "Hello World"}

@router.post("/reserve")
def reserve_table():
  """
  You can reserve a table by providing the table number
  """
  return {"message": "Hello World"}

@router.post("/release")
def release_table():
  """
  You can release a table by providing the table number
  This will make the table available for other customers
  This will also automatically generate a bill for the customer
  """
  return {"message": "Hello World"}