FROM python:3.12-slim
WORKDIR /app

RUN pip install --no-cache-dir flask redis gunicorn

COPY pyproject.toml ./
COPY src ./src
RUN pip install --no-cache-dir .

COPY app.py .

EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]