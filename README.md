# Task Manager API

A production-style RESTful Task Management API built with **Django** and **Django REST Framework**.

The project is being developed as a complete backend application with authentication, authorization, task management, filtering, searching, pagination, automated testing, and eventually PostgreSQL, Docker, CI/CD, and a SwiftUI client.

## Features

### Authentication

* User registration
* JWT authentication
* Login and token refresh
* Protected API endpoints
* User-specific data access

### Task Management

* Create tasks
* Retrieve tasks
* Update tasks
* Delete tasks
* Mark tasks as completed
* User-owned tasks

### API Features

* Pagination
* Filtering by completion status
* Search by title and description
* User-based querysets
* Permission-based access control

### Testing

The project includes automated tests covering:

* User registration
* Password hashing
* User login
* Invalid login credentials
* Task creation
* Authentication requirements
* Task ownership
* Task updates
* Task deletion
* Completing tasks
* Pagination

## Tech Stack

* Python
* Django
* Django REST Framework
* Simple JWT
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
│   └── tests.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## API Endpoints

### Authentication

| Method | Endpoint              | Description                  |
| ------ | --------------------- | ---------------------------- |
| POST   | `/api/auth/register/` | Register a new user          |
| POST   | `/api/auth/login/`    | Login and receive JWT tokens |
| POST   | `/api/auth/refresh/`  | Refresh an access token      |

### Tasks

| Method | Endpoint                    | Description                         |
| ------ | --------------------------- | ----------------------------------- |
| GET    | `/api/tasks/`               | List the authenticated user's tasks |
| POST   | `/api/tasks/`               | Create a task                       |
| GET    | `/api/tasks/<id>/`          | Retrieve a task                     |
| PUT    | `/api/tasks/<id>/`          | Update a task                       |
| PATCH  | `/api/tasks/<id>/`          | Partially update a task             |
| DELETE | `/api/tasks/<id>/`          | Delete a task                       |
| POST   | `/api/tasks/<id>/complete/` | Mark a task as completed            |

## Authentication

Protected endpoints require a JWT access token.

Include the token in the request header:

```text
Authorization: Bearer <access_token>
```

Example:

```text
GET /api/tasks/
Authorization: Bearer eyJ...
```

## Filtering

Tasks can be filtered by completion status.

Completed tasks:

```text
GET /api/tasks/?completed=true
```

Incomplete tasks:

```text
GET /api/tasks/?completed=false
```

## Search

Search tasks by title or description:

```text
GET /api/tasks/?search=django
```

Search can also be combined with filtering:

```text
GET /api/tasks/?search=django&completed=true
```

## Pagination

The API returns a maximum of 10 tasks per page.

```text
GET /api/tasks/
```

A paginated response contains:

```json
{
    "count": 12,
    "next": "...",
    "previous": null,
    "results": []
}
```

To request another page:

```text
GET /api/tasks/?page=2
```

## Local Development

### 1. Clone the repository

```bash
git clone <repository-url>
cd task-manager-api
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Run migrations

```powershell
python manage.py migrate
```

### 5. Start the development server

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

Run only user tests:

```powershell
python manage.py test users
```

Run only task tests:

```powershell
python manage.py test tasks
```

## Roadmap

The project will continue to evolve toward a production-ready backend.

### Completed

* [x] Django project setup
* [x] Custom User model
* [x] User registration
* [x] JWT authentication
* [x] Task CRUD
* [x] User task ownership
* [x] Task completion endpoint
* [x] Pagination
* [x] Task filtering
* [x] Task search
* [x] Automated tests

### Planned

* [ ] Advanced filtering with `django-filter`
* [ ] Ordering and sorting
* [ ] Better validation and error handling
* [ ] Password change/reset
* [ ] Token blacklisting/logout
* [ ] API documentation
* [ ] PostgreSQL
* [ ] Environment-based configuration
* [ ] Docker
* [ ] GitHub Actions CI
* [ ] Production deployment
* [ ] SwiftUI iOS client

## Project Goal

The goal of this project is to build a complete, production-style backend while following real-world development practices such as:

* REST API design
* Authentication and authorization
* Database design
* Automated testing
* Git version control
* Continuous integration
* Containerization
* Production deployment

Eventually, the API will be consumed by a native **SwiftUI iOS application**.
