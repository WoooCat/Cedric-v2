# Online Store API

## Description:

The Online Store API is RESTful API for managing categories, products, discounts, reservations, sales in online store.
The API is built with FastAPI and uses PostgreSQL for data storage.

## Technologies

- **FastAPI**: Framework for building fast APIs in Python.
- **PostgreSQL**: Relational database for data storage.
- **SQLAlchemy**: ORM for interacting with the database.
- **Pydantic**: Library for data validation.
- **Docker**: Containerization for ease of deployment.
- **pytest**: Framework for testing.



## DOCUMENTATION : [Swagger UI](http://localhost:8000/docs)
#### Documentation will be available after the start of the service
#### OR just open this url: [http://localhost:8000/docs](https://localhost:8000/docs)


## HOW TO USE:
### RUN Local:

```bash
uvicorn main:app --reload --port 8000
```

### USE in Docker:

```bash
# Use 'make help' to view all commands
make help

# run API in Docker
make start

# shutdown API in Docker
make stop
```