# 🎬 Full-Stack Personal Media Cataloging Platform

A modern, highly performant Single Page Application (SPA) designed to dynamically catalog, monitor, and query multimedia assets. The system implements a robust, asynchronous RESTful API architecture combined with a normalized object-relational database persistence layer and a responsive, zero-refresh reactive user interface.

## 🛠️ System Architecture & Engineering Highlights

* **Asynchronous Web Framework:** Engineered utilizing **FastAPI** to enable high-throughput concurrency, structured data verification, and automatic documentation serialization.
* **Modern ORM Architecture:** Leverages **SQLModel** (combining SQLAlchemy and Pydantic primitives) to maintain strict type safety, automatic schemas, and a unified data model across database and API barriers.
* **Modern Lifespan Management:** Replaces legacy startup events with an advanced `asynccontextmanager` context lifecycle to explicitly manage database tables dynamically upon backend initialization.
* **Dynamic Frontend Data Flow:** Implements a decoupled client-side JavaScript architecture utilizing asynchronous `fetch` logic mapping directly to `POST`, `GET`, `PATCH`, and `DELETE` REST endpoints.
* **Dynamic Form Lifecycle Control:** Features event-driven DOM manipulation that updates form field validation states reactively (e.g., dynamic dependency logic handling for author fields based on media categories).
* **Modern CSS Engine:** Designed natively with **Tailwind CSS v4** utilizing component utility classes for visual fluidity and modern interface structures.

## 📋 Technology Stack Stack

* **Backend Engine:** Python 3.11+ / FastAPI
* **Database & ORM layer:** SQLModel / SQLite
* **Frontend Architecture:** Native JavaScript (ES6+ Asynchronous DOM) / Tailwind CSS v4
* **API Paradigm:** REST (JSON Payloads)

## 📡 REST API Endpoint Architecture

| HTTP Method | API Path | Core Backend Operations & Business Logic |
| :--- | :--- | :--- |
| `POST` | `/media/` | Materializes and serializes a new media entry into the relational database. |
| `GET` | `/media/` | Queries and fetches the complete list array of stored media models. |
| `GET` | `/media/{media_id}` | Retrieves a granular single record; executes explicit `404 Error` handling if not found. |
| `PATCH` | `/media/{media_id}` | Performs a partial delta modification via `model_dump(exclude_unset=True)`. |
| `DELETE` | `/media/{media_id}` | Purges a specific indexed table row by its primary key mapping constraint. |
| `DELETE` | `/media/` | Global purge operation; clears all populated schema items simultaneously. |

## 🚀 Local Deployment Setup

Ensure you have Python installed on your system before proceeding with the deployment commands below.

### 1. Clone the Codebase
```bash
git clone https://github.com
cd YOUR_REPOSITORY_NAME
```

### 2. Set Up Virtual Environment & Dependencies
```bash
# Create environment
python -m venv venv

# Activate environment (Windows)
venv\Scripts\activate

# Activate environment (macOS/Linux)
source venv/bin/activate

# Install required architecture frameworks
pip install fastapi sqlmodel uvicorn jinja2
```

### 3. Initialize the Application Server
Run the application server using Uvicorn with auto-reload enabled for development tracking:
```bash
uvicorn main:app --reload
```
Once initialized, navigate your local web browser directory path to: `http://127.0.0`

## 📈 Planned Structural Enhancements
* Refactor database connections to utilize completely asynchronous engine engines (`ext.asyncio`).
* Integrate a secured user authorization protocol via OAuth2 and JWT bearer tokens.
* Develop specialized multi-column search sorting options across relational database tables.
