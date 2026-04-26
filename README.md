# E-Commerce REST API

A production-grade Django REST Framework API for e-commerce applications with secure authentication, inventory management, and order processing.

---

## Key Architecture & Features

- **Relational Schema with Data Integrity**: Foreign key relationships enforce CASCADE and PROTECT constraints to maintain referential integrity across orders, products, and users.
- **Abstract TimeStamped Models**: Core abstract base model provides `created_at` and `updated_at` fields inherited by all domain models.
- **Real-time Inventory Engine**: Uses `transaction.atomic()` to handle nested JSON payloads safely, preventing race conditions during concurrent stock updates.
- **Custom Email-Based User Model**: Extends `AbstractUser` with email as the primary authentication field, secured via JWT tokens.
- **Data Isolation**: Strict query filtering ensures users can only access their own orders and data.
- **Environment Variable Management**: All secrets and configuration managed via `.env` files using `django-environ`.

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Framework | Django 5.2 + Django REST Framework |
| Language | Python 3.11+ |
| Authentication | JWT (djangorestframework-simplejwt) |
| Database | PostgreSQL (psycopg) |
| Configuration | django-environ |

---

## Local Setup & Installation

```powershell
# Clone the repository
git clone <repository-url>
cd ecom_engine

# Create virtual environment
python -m venv venv
.\venv\Scripts\Activate

# Install dependencies
pip install -r requirements.txt

# Create .env file in project root
# Add the following variables:
# DEBUG=True
# SECRET_KEY=your-secret-key-here
# DATABASE_URL=postgres://user:password@localhost:5432/ecom_db

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

---

## API Endpoints Overview

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/token/` | POST | Obtain JWT token pair (access + refresh) |
| `/api/token/refresh/` | POST | Refresh access token |
| `/api/products/` | GET, POST | List all products / Create new product |
| `/api/orders/` | GET, POST | List user's orders / Create new order |

---

## Future Scope & Roadmap

### Phase 1: API Polish & Data Handling

- **[In Progress] Image & Media Handling**: Configuring the Pillow library and Django's media settings to securely upload, validate, and serve product image URLs through the API.
- **[Planned] Advanced API Optimization**: Implementing DRF Pagination (e.g., Cursor or LimitOffset) and integrating django-filter to allow dynamic search, sorting, and filtering for large product catalogs without crashing the server.

### Phase 2: The Checkout & Communication Pipeline

- **[Planned] Payment Gateway Integration**: Simulating live financial transactions by integrating Stripe or Razorpay APIs, utilizing secure Webhooks to automatically transition database order statuses from PENDING to PAID.
- **[Planned] Asynchronous Task Queues**: Setting up Celery with a RabbitMQ or Redis broker to offload heavy processes—such as sending order confirmation emails and generating PDF invoices—to the background, ensuring the main API remains lightning-fast.

### Phase 3: Performance & Scalability (DevOps)

- **[Planned] Distributed Caching Layer**: Implementing Redis to cache high-traffic, read-heavy endpoints (like the main product catalog), drastically reducing direct query load on the PostgreSQL vault.
- **[Planned] Application Containerization**: Writing Dockerfile and docker-compose.yml configurations to containerize the entire stack (Django, PostgreSQL, Redis, Celery), ensuring consistent, isolated deployment across any environment.
- **[Planned] CI/CD Pipeline Automation**: Establishing GitHub Actions to create a continuous integration pipeline that automatically runs unit tests, database migration checks, and code linting on every repository push.

### Phase 4: The Intelligence Layer (Bonus Feature)

- **[Planned] AI-Powered Recommendation Engine**: Developing a custom endpoint that analyzes order history patterns (or uses lightweight vector similarity) to generate "Frequently Bought Together" or "Recommended for You" product suggestions.