import json
import logging


logger = logging.getLogger(__name__)

def transform_menu_json():
  flat_menu = []
  with open('data/menu.json') as f:
    data = json.load(f)
    if "categories" in data:
      for category_name,category_items in data["categories"].items():
        logger.info(f"Category: {category_name}")
        for item_number, item in enumerate(category_items):
          name = item["name"]
          price = item["price"]
          flat_menu.append({
            "category": category_name,
            "item_id": f"{category_name}_{item_number}",
            "name": name,
            "price": price
          })
  
  menu = {
    "items": flat_menu
  }
  
  with open('data/menu_flat.json', 'w') as f:
    json.dump(menu, f, indent=2)
    logger.info("Transformed data written to data/menu_flat.json")