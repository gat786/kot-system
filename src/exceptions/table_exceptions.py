class TablesNotDefined(Exception):
  def __init__(self):
    return
  def __str__(self):
    return f"Tables are not yet setup properly"

class TableNotFound(Exception):
  def __init__(self, table_id):
    self.table_id = table_id

  def __str__(self):
    return f"Table {self.table_id} not found"