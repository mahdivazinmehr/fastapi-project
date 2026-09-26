# FastAPI Project

A simple REST API for managing products, built with FastAPI, SQLAlchemy and SQLite.

## Features

* Create, read, update and delete products
* Filter products by category
* Input validation
* Basic error handling

## Technologies

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic

## Setup

Clone the repository:

```bash
git clone https://github.com/mahdivazinmehr/fastapi-project.git
cd fastapi-project
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn main:app --reload
```

## API Docs

Swagger UI:

`http://127.0.0.1:8000/docs`

## Endpoints

`GET /` - Welcome message

`POST /products` - Create a product

`GET /products` - Get products

`GET /products/{id}` - Get a product by ID

`PUT /products/{id}` - Update a product

`DELETE /products/{id}` - Delete a product
