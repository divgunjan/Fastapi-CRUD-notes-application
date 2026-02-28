
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

## Testing with Postman

1. Open Postman and create a new request
2. Set the request type (GET, POST, PUT, or DELETE)
3. Enter the URL: `http://localhost:8000/notes` (or with `/{id}` for specific operations)
4. For POST/PUT requests, go to the **Body** tab, select **raw**, choose **JSON**, and add your note data
5. Click **Send** to execute the request

## Documentation

- Interactive API docs: `http://localhost:8000/docs`
- Alternative docs: `http://localhost:8000/redoc`

