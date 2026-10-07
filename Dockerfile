
FROM python:3.14-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.14-slim

WORKDIR /app

COPY --from=builder /install /usr/local
COPY app ./app

RUN useradd --create-home --shell /usr/sbin/nologin appuser && chown -R appuser:appuser /app

USER appuser

EXPOSE 5000

CMD ["python", "-m", "app.main"]