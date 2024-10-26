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
        for item in category_items:
          name = item["name"]
          price = item["price"]
          flat_menu.append({
            "category": category_name,
            "name": name,
            "price": price
          })
  
  with open('data/menu_flat.json', 'w') as f:
    json.dump(flat_menu, f, indent=2)
    logger.info("Transformed data written to data/menu_flat.json")