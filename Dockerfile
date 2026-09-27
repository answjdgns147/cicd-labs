FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir --upgrade "msgpack>=1.2.1" "setuptools>=78.1.1"

# TEMP: print installed versions in build log for verification
RUN pip show msgpack setuptools

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
