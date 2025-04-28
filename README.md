# Master-Slave-database Replication
🔗 **Medium Blog link :** [Blog Link] (https://medium.com/@abhijeet.sarkar112/how-i-set-up-postgresql-streaming-replication-on-windows-primary-replica-on-same-machine-e0ad35e029db)
## FastAPI Read/Write Split Example

This is a simple FastAPI application that:
- **Writes** data to a **Primary PostgreSQL** database.
- **Reads** data from a **Replica PostgreSQL** database.

It uses **SQLAlchemy** as the database ORM and **Pydantic** for request validation.

---

## 📚 Requirements

- Python 3.8+
- PostgreSQL (Primary and Replica)
- FastAPI
- SQLAlchemy
- psycopg2-binary
- uvicorn (for running the server)

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
2.Create a virtual environment:
```bash
  python -m venv venv
  source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

3.Install dependencies:
```bash
   pip install -r requirements.txt
```

🚀 Running the app
Use uvicorn to start the FastAPI development server:
```bash
uvicorn main:app --reload
```

##📋 API Endpoints
POST /write-data
Description:
Insert a new record into the Primary database.

Request Body:
```json
{
  "name": "John Doe"
}
```
Response:
```json
{
  "message": "Data 'John Doe' written to primary"
}
```

##GET /read-data
Description:
Fetches up to 10 records from the Replica database.

Response:
```json
{
  "data": [
    {
      "id": 1,
      "name": "John Doe"
    },
    {
      "id": 2,
      "name": "Jane Doe"
    }
  ]
}
```

