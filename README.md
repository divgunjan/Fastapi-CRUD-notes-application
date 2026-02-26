
# Notes CRUD API

A simple CRUD (Create, Read, Update, Delete) API for managing notes built with FastAPI.

## Features

- Create new notes
- Read/retrieve notes
- Update existing notes
- Delete notes

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Pydantic

## Installation

```bash
pip install fastapi uvicorn
```

## Running the Server

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/notes` | Create a new note |
| GET | `/notes` | Get all notes |
| GET | `/notes/{id}` | Get a specific note |
| PUT | `/notes/{id}` | Update a note |
| DELETE | `/notes/{id}` | Delete a note |

## Documentation

- Interactive API docs: `http://localhost:8000/docs`
- Alternative docs: `http://localhost:8000/redoc`
