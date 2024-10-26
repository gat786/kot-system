FROM python:3.12

RUN pip install uv

# Set the working directory
WORKDIR /app

# Copy the pyproject.toml and uv.lock files
COPY pyproject.toml .
COPY uv.lock .

# Install the dependencies
RUN uv sync

# Copy the rest of the files
COPY . .

# Run http server
CMD ["uv", "run", "src/main.py", "run-server"]