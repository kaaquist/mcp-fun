# Install UV 
FROM python:3.11-bullseye
COPY --from=ghcr.io/astral-sh/uv:0.6.3 /uv /bin/uv

ENV PYTHONUNBUFFERED True
ENV ENVIRONMENT production

WORKDIR /opt

# Copy the lockfile and `pyproject.toml` into the image
COPY uv.lock /opt/uv.lock
COPY pyproject.toml /opt/pyproject.toml

# Install dependencies
RUN uv sync --frozen --no-install-project

COPY main.py /opt/app/
COPY LICENSE /opt/LICENSE
COPY README.md /opt/README.md

# Sync the project
RUN uv sync --frozen
ENV PATH="/opt/.venv/bin:$PATH"

EXPOSE 8000

CMD ["uv", "run", "/opt/app/main.py"]