from dataclasses import dataclass
from typing import List
from pydantic import BaseModel

@dataclass
class MenuItem(BaseModel):
  category: str
  item_id: str
  name: str
  price: float

@dataclass
class Menu(BaseModel):
  items: List[MenuItem]

  def get_item(self, item_id: str):
    for item in self.items:
      if item.item_id == item_id:
        return item
    return None