from fastapi import APIRouter
from models import menu
import json

router = APIRouter(
  prefix="/menu"
)

@router.get("/")
def get_menu():
  """
  This will return the menu, this will have entire menu
  """
  try:
    with open("data/menu_flat.json") as f:
      data = f.read()
      menu_model = menu.Menu.model_validate_json(data)
      return menu_model
  except FileNotFoundError:
    return {
      "message": "Menu not found, make sure you have run the transformer script"
    }

@router.get("/item/{item_id}")
def get_menu_item(item_id: str):
  """
  This will return the single item for which you provide an item_id
  """
  try:
    with open("data/menu_flat.json") as f:
      data = f.read()
      menu_model = menu.Menu.model_validate_json(data)
      selected_item = [item for item in menu_model.items if item.item_id == item_id]
      return selected_item
  except FileNotFoundError:
    return {
      "message": "Menu not found, make sure you have run the transformer script"
    }


@router.get("/{category}")
def get_category(category: str):
  """
  This will return the menu, this will have entire menu
  """
  try:
    with open("data/menu_flat.json") as f:
      data = f.read()
      menu_model = menu.Menu.model_validate_json(data)
      selected_item = [item for item in menu_model.items if item.category == category]
      return selected_item
  except FileNotFoundError:
    return {
      "message": "Menu not found, make sure you have run the transformer script"
    }
  

