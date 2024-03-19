FROM python:3.10

# Configure Poetry
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.8.2
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/venv
ENV POETRY_CACHE_DIR=/opt/.cache


COPY ./api-pontos-turisticos /api-pontos-turisticos
COPY ./scripts /scripts

WORKDIR /api-pontos-turisticos

EXPOSE 8005

# Install dependencies
RUN python3 -m venv $POETRY_VENV && . $POETRY_VENV/bin/activate  && \
  $POETRY_VENV/bin/pip install --upgrade pip && \
  $POETRY_VENV/bin/pip install -U pip setuptools && \
  $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION} && \
  $POETRY_VENV/bin/poetry config virtualenvs.path  $POETRY_VENV && \
  poetry install --no-root && \
  adduser --disabled-password --no-create-home duser && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  chown -R duser:duser  $POETRY_VENV && \
  chown -R duser:duser /data/web/static && \
  chown -R duser:duser /data/web/media && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /data/web/media && \
  chmod -R +x /scripts


# Adiciona a pasta scripts e venv/bin
# no $PATH do container.
ENV PATH="/scripts:${POETRY_VENV}/bin:$PATH"

# Muda o usuário para duser
USER duser

# Executa o arquivo scripts/commands.sh
CMD ["run.sh"]