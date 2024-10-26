from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class Table(BaseModel):
  table_id: int
  seating_capacity: int
  location: str
  is_reserved: bool = False
  reservation_details: dict | None = None

@dataclass
class Tables(BaseModel):
  tables: list[Table]

@dataclass
class TableReserveModel(BaseModel):
  table_id: int