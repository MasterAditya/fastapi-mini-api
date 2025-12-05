# 🚀 FastAPI Mini API: The Microservice Accelerator

A clean, modular, and production-ready boilerplate for building high-performance Python microservices. Perfect for rapid prototypes, SaaS features, or freelance contracts.

---

## 📖 About This Project

The **FastAPI Mini API** is designed for developers who need to ship functional backend code quickly.  
It moves beyond the basic "Hello World" example by providing a structured foundation that is **scalable** and **maintainable**.

**Use Cases:**
- **Rapid Prototyping (MVPs):** Get your core API endpoints functional in minutes.
- **Microservices:** Build small, focused services that integrate into a larger system.
- **Freelance Starter Kit:** A pre-vetted base for any new Python project.

---

## ✨ Core Features

- **Ready-to-Go Endpoints:** Includes basic `/ping` (GET) and `/data` (POST) endpoints.
- **Modular Design:** Logic separated into `main.py`, `routes.py`, `models.py`, and `utils.py`.
- **Pydantic Validation:** Ensures data integrity for all requests and responses.
- **Auto-Generated Docs:** Instant access to Swagger UI (`/docs`) and ReDoc (`/redoc`).
- **Developer Experience:** Uvicorn is configured with hot-reloading (`--reload`) for fast development cycles.

---

## 📂 Project Structure

```
fastapi-mini-api/
├── app/
│   ├── main.py          # Application entry point (initializes FastAPI app)
│   ├── routes.py        # Defines all core API endpoints
│   ├── models.py        # Pydantic Schemas for data validation
│   └── utils.py         # Placeholder for business logic and helper functions
├── requirements.txt     # Project dependencies list
├── .gitignore          # Files ignored by Git
└── README.md           # This documentation file
```

---

## 🛠 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/MasterAditya/fastapi-mini-api.git
cd fastapi-mini-api
```

### 2. Install Dependencies

Using a virtual environment is highly recommended:

```bash
pip install -r requirements.txt
```

### 3. Run the Server

Start the application using Uvicorn:

```bash
uvicorn app.main:app --reload
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description                  | Payload Example                  |
|--------|----------|------------------------------|----------------------------------|
| GET    | /ping    | A standard server health check | None                             |
| POST   | /data    | Accepts and validates a simple string value | `{ "value": "New Data Payload" }` |

💡 **Documentation:** Visit [Swagger UI](http://127.0.0.1:8000/docs) to interact with the API.

---

## 💻 Tech Stack

| Technology | Role                                      |
|------------|-------------------------------------------|
| FastAPI    | Core high-performance Python web framework |
| Pydantic   | Data validation and configuration management |
| Uvicorn    | Asynchronous Server Gateway Interface (ASGI) server |

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
