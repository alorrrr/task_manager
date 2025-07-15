FROM python:3.13.2-slim 

WORKDIR /app
ENV PYTHONUNBUFFERED=1 
ENV PYTHONDONTWRITEBYTECODE=1

COPY pyproject.toml poetry.lock ./
RUN pip install --upgrade pip && pip install --no-cache-dir poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 8000
