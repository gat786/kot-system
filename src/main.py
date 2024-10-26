from utils import environments, setup_logging
from typer import Typer
from fastapi import FastAPI
import uvicorn

cli = Typer(
  invoke_without_command=True,
  no_args_is_help=True
)
api = FastAPI()

@cli.command()
def migrate():
  """
  This is ran to run migration scripts to setup database
  """
  pass

@cli.command()
def run_server():
  """
  This will start an HTTP server on localhost and PORT
  """
  uvicorn.run(
    "main:api",
    host="localhost",
    port=int(environments.SERVER_PORT),
  )
  pass


if __name__ == "__main__":
  cli()
