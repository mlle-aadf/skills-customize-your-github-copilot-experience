# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI to practice endpoint design, request/response models, and basic in-memory data management.

## 📝 Tasks

### 🛠️ Create Core CRUD Endpoints

#### Description
Create an API for managing a small collection of books. You will define endpoints to create, read, update, and delete books.

#### Requirements
Completed program should:

- Implement `GET /books` to return all books.
- Implement `GET /books/{book_id}` to return one book by ID.
- Implement `POST /books` to create a new book.
- Implement `PUT /books/{book_id}` to update an existing book.
- Implement `DELETE /books/{book_id}` to delete a book.


### 🛠️ Add Validation and Proper HTTP Responses

#### Description
Use Pydantic models to validate request data and return meaningful status codes and errors.

#### Requirements
Completed program should:

- Define a Pydantic model with fields: `title`, `author`, and `year`.
- Validate that `year` is a reasonable value (for example, greater than 0).
- Return `404` for requests targeting a non-existent `book_id`.
- Return `201` when a book is created successfully.
- Return JSON responses in a consistent format.