# Use an official Python runtime as a parent image
FROM python:3.12-slim

RUN pip install --no-cache-dir poetry

# Set the working directory in the container
WORKDIR /app

COPY pyproject.toml poetry.lock* /app/
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-dev

COPY . /app

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable for Uvicorn
ENV HOST=0.0.0.0
ENV PORT=8000

# Run app.py when the container launches
CMD ["uvicorn", "espia_jogos.api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
