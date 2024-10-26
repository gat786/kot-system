from fastapi import APIRouter, Response
from models import table as table_models
from repository import tables as tables_repo
import logging
import json

router = APIRouter(
  prefix="/tables"
)
logger = logging.getLogger(__name__)

tables = tables_repo.Tables()

@router.get("/")
def get_tables():
  """
  This will return all the tables
  This will give you information regarding what is the current
  status of table i.e. whether it is reserved or not.
  """
  return tables.get_tables()

@router.post("/reserve")
def reserve_table(reserve_details: table_models.TableReserveModel):
  """
  You can reserve a table by providing the table number
  """
  logger.info(f"Reserving table {reserve_details.table_id}")
  try:
    reserved = tables.reserve_table(
      table_id=reserve_details.table_id
    )
    return {"reserved": reserved}
  except tables_repo.TableNotFound as e:
    return Response(
      status_code=404, 
      content=json.dumps({
      "message": f"Table {e.table_id} not found"
      }),
      media_type="application/json"
    )

@router.post("/release")
def release_table():
  """
  You can release a table by providing the table number
  This will make the table available for other customers
  This will also automatically generate a bill for the customer
  """
  return {"message": "Hello World"}