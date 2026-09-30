FROM python:3.13-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1

# Install dependencies into an isolated venv, then drop pip from it
RUN python -m venv /opt/venv
COPY requirements.txt .
RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt \
    && /opt/venv/bin/pip uninstall -y pip


FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

# Apply the latest OS security patches (e.g. OpenSSL) at build time
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

# Remove pip (and ensurepip's bundled pip wheel) shipped with the base image
RUN python -m pip uninstall -y pip \
    && rm -rf /usr/local/lib/python3.13/ensurepip/_bundled

COPY --from=builder /opt/venv /opt/venv

WORKDIR /app
COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
