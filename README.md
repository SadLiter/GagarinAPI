# GagarinAPI

GagarinAPI is a simple API providing facts about Yuri Gagarin, the first human in space. It uses Flask for the backend, MongoDB for data storage, and Docker for containerization. Basic API tests are included to verify functionality.

## Features

- Random fact about Yuri Gagarin.
- Retrieve all facts.
- Fetch random facts by category (e.g., "space", "biography").
- Dockerized for easy deployment.
- Includes API tests for validation.

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SadLiter/GagarinAPI.git
   cd GagarinAPI
   ```

2. **Build and run with Docker Compose**:
   ```bash
   docker-compose up --build
   ```

3. **Access the API**:  
   The API will be running at `http://localhost:5000`.

4. **Run tests**:
   To run the tests for the API:
   ```bash
   pytest
   ```

## Endpoints

- **GET /random_fact**: Get a random fact about Yuri Gagarin.
- **GET /all_facts**: Get all facts.
- **GET /random_fact_by_category?category=<category>**: Get a random fact by category (e.g., "space", "biography").

## Technologies

- **Flask**: Python web framework.
- **MongoDB**: Database for storing facts.
- **Docker**: Containerization.
- **pytest**: For testing the API.
