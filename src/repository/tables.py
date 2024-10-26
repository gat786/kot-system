import logging
from exceptions.table_exceptions import TableNotFound, TablesNotDefined
from models import table as table_models

logger = logging.getLogger(__name__)

def get_tables_data():
  try:
    with open("data/tables.json") as f:
      data = f.read()
      return data
  except FileNotFoundError:
    logger.info("Tables not found, make sure you have tables.json in data directory")
    return None

class Tables:

  def __init__(self) -> None:
    tables_data = get_tables_data()
    if tables_data is None:
      self.tables = None
    else:
      self.tables = table_models.Tables.model_validate_json(tables_data)

  def get_tables(self):
    return self.tables

  def reserve_table(self, table_id: int) -> bool:
    logger.debug(f"Reserving table {table_id}")
    if self.tables is None:
      raise TablesNotDefined()
    for table in self.tables.tables:
      if table.table_id == table_id:
        table.is_reserved = True
        return True
    raise TableNotFound(table_id=table_id)
    