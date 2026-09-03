# Task Manager API

A production-style REST API built with Django and Django REST Framework.

The project provides user authentication, secure task ownership, CRUD operations, filtering, search, ordering, pagination, and automated testing.

## Features

### Authentication

* User registration
* JWT login
* JWT token refresh
* Password hashing
* Protected API endpoints

### Task Management

* Create tasks
* View tasks
* Update tasks
* Delete tasks
* Mark tasks as completed
* Users can only access their own tasks

### Querying

* Filter tasks by completion status
* Search tasks by title and description
* Order tasks by different fields
* Pagination

### Testing

* Automated API tests using Django REST Framework
* Authentication tests
* Permission and ownership tests
* CRUD tests
* Filtering, search, and ordering tests
* Pagination tests
* **14 tests currently passing**

## Tech Stack

* Python
* Django
* Django REST Framework
* Simple JWT
* django-filter
* SQLite (development)
* Git / GitHub

## Project Structure

```text
task-manager-api/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── users/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── tasks/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── manage.py
├── requirements.txt
└── README.md
```

## API Endpoints

### Authentication

| Method | Endpoint              | Description                  |
| ------ | --------------------- | ---------------------------- |
| POST   | `/api/auth/register/` | Register a new user          |
| POST   | `/api/auth/login/`    | Login and receive JWT tokens |
| POST   | `/api/auth/refresh/`  | Refresh access token         |

### Tasks

| Method | Endpoint                    | Description              |
| ------ | --------------------------- | ------------------------ |
| GET    | `/api/tasks/`               | List user's tasks        |
| POST   | `/api/tasks/`               | Create a task            |
| GET    | `/api/tasks/{id}/`          | Retrieve a task          |
| PUT    | `/api/tasks/{id}/`          | Update a task            |
| PATCH  | `/api/tasks/{id}/`          | Partially update a task  |
| DELETE | `/api/tasks/{id}/`          | Delete a task            |
| POST   | `/api/tasks/{id}/complete/` | Mark a task as completed |

## Filtering

Filter tasks by completion status:

```text
GET /api/tasks/?completed=true
```

or:

```text
GET /api/tasks/?completed=false
```

## Search

Search by task title or description:

```text
GET /api/tasks/?search=django
```

## Ordering

Order tasks by title:

```text
GET /api/tasks/?ordering=title
```

Newest tasks first:

```text
GET /api/tasks/?ordering=-created_at
```

Filtering, search, and ordering can also be combined:

```text
GET /api/tasks/?completed=false&search=django&ordering=title
```

## Pagination

Tasks are paginated with a default page size of 5.

```text
GET /api/tasks/
```

Next pages can be accessed using:

```text
GET /api/tasks/?page=2
```

The API returns:

```json
{
    "count": 10,
    "next": "...",
    "previous": null,
    "results": []
}
```

## Authentication

Task endpoints require authentication.

Include the JWT access token in the request:

```text
Authorization: Bearer <access_token>
```

Users can only access and modify tasks that belong to them.

## Running Locally

Clone the repository and navigate into the project:

```bash
git clone <repository-url>
cd task-manager-api
```

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run migrations:

```powershell
python manage.py migrate
```

Start the development server:

```powershell
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

## Running Tests

Run the complete test suite:

```powershell
python manage.py test
```

Current status:

```text
14 tests passed
```

## Roadmap

Planned improvements include:

* Advanced task filtering with custom FilterSets
* Task priorities
* Due dates
* Categories
* Better validation and error handling
* Password change and password reset
* JWT logout / token blacklisting
* API documentation with OpenAPI / Swagger
* PostgreSQL
* Environment-based configuration
* Docker
* GitHub Actions CI
* Production deployment
* SwiftUI iOS client

## Goal

The goal of this project is to build a complete, production-style Django REST API while following professional development practices such as:

* Clean architecture
* Authentication and authorization
* Automated testing
* API design
* Database design
* Documentation
* CI/CD
* Containerization
* Production deployment
