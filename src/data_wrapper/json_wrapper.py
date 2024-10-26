import json

def get_menu_items():
  try:
    with open("data/menu_flat.json") as f:
      data = f.read()
      return data
  except FileNotFoundError:
    return {
      "message": "Menu not found, make sure you have run the transformer script"
    }