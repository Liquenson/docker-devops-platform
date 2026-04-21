from fastapi import FastAPI
import os
import psycopg2
import time

app = FastAPI()


def get_db_connection(retries=5, delay=2):
    for _ in range(retries):
        try:
            return psycopg2.connect(
                host=os.getenv("DB_HOST") or "db",
                port=int(os.getenv("DB_PORT") or 5432),
                dbname=os.getenv("DB_NAME") or "app_db",
                user=os.getenv("DB_USER") or "app_user",
                password=os.getenv("DB_PASSWORD") or "secure_password",
            )
        except Exception:
            time.sleep(delay)
    raise Exception("Database connection failed")


@app.get("/")
def root():
    return {"message": "Docker DevOps Platform Running"}


@app.get("/health")
def health():
    try:
        conn = get_db_connection()
        conn.close()
        return {"status": "ok", "db": "connected"}
    except Exception as e:
        return {"status": "error", "db": str(e)}
