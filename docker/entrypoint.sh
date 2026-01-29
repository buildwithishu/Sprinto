#!/usr/bin/env bash
set -e

if [ "${DB_ENGINE}" = "postgres" ]; then
  echo "Waiting for Postgres..."
  python - <<'PY'
import os
import time
import psycopg2
from psycopg2 import OperationalError

host = os.environ.get("DB_HOST", "db")
port = os.environ.get("DB_PORT", "5432")
name = os.environ.get("DB_NAME", "postgres")
user = os.environ.get("DB_USER", "postgres")
password = os.environ.get("DB_PASSWORD", "")
timeout = int(os.environ.get("DB_WAIT_TIMEOUT", "60"))
start = time.time()

while True:
    try:
        conn = psycopg2.connect(
            dbname=name,
            user=user,
            password=password,
            host=host,
            port=port,
        )
        conn.close()
        print("Postgres is available.")
        break
    except OperationalError as exc:
        if time.time() - start > timeout:
            raise
        time.sleep(2)
PY
fi

if [ "${RUN_MAKEMIGRATIONS:-0}" = "1" ]; then
  python manage.py makemigrations --noinput
fi

if [ "${RUN_MIGRATIONS:-0}" = "1" ]; then
  python manage.py migrate --noinput
fi

exec "$@"
