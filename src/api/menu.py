from fastapi import APIRouter

router = APIRouter(
  prefix="/menu"
)

@router.get("/")
def get_menu():
  """
  This will return the menu, this will have entire menu
  """
  return {"message": "Hello World"}


@router.get("/{category_id}")
def get_category(category_id: str):
  """
  This will return the menu, this will have entire menu
  """
  return {"message": "Hello World"}

