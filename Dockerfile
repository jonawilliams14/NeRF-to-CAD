FROM python:3.11-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends colmap \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml README.md requirements.txt ./
COPY coffee_nerf_cad ./coffee_nerf_cad
RUN python -m pip install --no-cache-dir -U pip \
    && python -m pip install --no-cache-dir -e .[mesh,cad]

COPY . .

ENTRYPOINT ["coffee-nerf-cad"]
