from fastapi import FastAPI
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

app = FastAPI()

DATABASE_URL_PRIMARY = "postgresql://replicator:yourpassword@127.0.0.1:5433/postgres"
DATABASE_URL_REPLICA = "postgresql://replicator:yourpassword@127.0.0.1:5434/postgres"

primary_engine = create_engine(DATABASE_URL_PRIMARY)
replica_engine = create_engine(DATABASE_URL_REPLICA)

PrimarySessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=primary_engine)
ReplicaSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=replica_engine)



# Pydantic model to accept data in the POST body
class User(BaseModel):
    name: str

@app.post("/write-data")
def write_data(user: User):
    session = PrimarySessionLocal()
    try:
        # Use the name provided in the request body and insert into primary DB
        session.execute(text("INSERT INTO demo (name) VALUES (:name)"), {"name": user.name})
        session.commit()
        return {"message": f"Data '{user.name}' written to primary"}
    finally:
        session.close()

@app.get("/read-data")
def read_data():
    session = ReplicaSessionLocal()
    try:
        result = session.execute(text("SELECT * FROM demo LIMIT 10")).fetchall()
        return {"data": [dict(row._mapping) for row in result]}

    finally:
        session.close()
