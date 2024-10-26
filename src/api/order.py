from fastapi import APIRouter
from typing import List

router = APIRouter(
  prefix="/order"
)

@router.post("/")
def create_order(
  reservation_id: str,
  menu_item_id: List[str],
):
  """
  This will create an order for the customer,
  Each reservation is a list of orders, so this will
  add an order to the reservation

  Once you release the table, a bill will be generated
  which will have all the orders for the reservation
  """
  return {"message": "Hello World"}