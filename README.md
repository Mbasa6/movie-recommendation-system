# Movie Recommendation System

## Project Overview
The Movie Recommendation System is a data science application that suggests movies to users based on their preferences, ratings, and viewing history.

The system analyzes movie datasets and user behavior to generate personalized recommendations using machine learning techniques.

---

## Project Goals
The goal of this project is to design and implement a recommendation system that improves the movie discovery experience for users.

The system will:
- Analyze movie ratings and genres
- Learn user preferences
- Generate personalized movie suggestions

---

## Technologies
The system uses the following technologies:

- Python
- FastAPI
- Machine Learning (Collaborative Filtering / Similarity Models)
- MovieLens Dataset
- Pytest
- GitHub for version control

---

## Documentation

Project documentation is organized by assignment:

### Assignment 3
- [System Specification](SPECIFICATION.md)
- [System Architecture](ARCHITECTURE.md)

### Assignment 4
- [Stakeholders](STAKEHOLDERS.md)
- [Requirements](REQUIREMENTS.md)

### Assignment 5
- [Use Case Diagram](USE_CASE_DIAGRAM.md)
- [Use Case Specifications](USE_CASE_SPECIFICATIONS.md)
- [Test Cases](TEST_CASES.md)

### Assignment 6
- [User Stories](USER_STORIES.md)
- [Product Backlog](PRODUCT_BACKLOG.md)
- [Sprint Plan](SPRINT_PLAN.md)

### Assignment 7
- [Template Analysis](template_analysis.md)
- [Kanban Explanation](kanban_explanation.md)
- [Kanban Board](KANBAN_BOARD.md)

### Assignment 8
- [State Diagrams](STATE_DIAGRAMS.md)
- [Activity Diagrams](ACTIVITY_DIAGRAMS.md)
- [Reflection](REFLECTION_A8.md)

### Assignment 9
- [Domain Model](DOMAIN_MODEL.md)
- [Class Diagram](CLASS_DIAGRAM.md)
- [Reflection](REFLECTION_A9.md)

### Assignment 10
- [Creational Patterns](creational_patterns/)
- [Tests](tests/)
- [Changelog](CHANGELOG.md)

### Assignment 11
- [Repositories](repositories/)
- [Repository Factory](factories/)
- [Repository Tests](tests/)

### Assignment 12
- [Service Layer](services/)
- [REST API](api/)
- [API Documentation](docs/API_DOCUMENTATION.md)
- [Swagger Screenshot](docs/swagger-ui-screenshot.png)

---

## Expected Features

- User login and profile
- Movie rating system
- Personalized movie recommendations
- Movie search and filtering
- REST API endpoints
- Swagger/OpenAPI documentation
- Repository pattern implementation
- Service layer business logic

---

## Assignment 10

### Language Used
Python was used for implementing the system due to its simplicity and strong support for object-oriented programming and testing.

### Class Implementation
All classes from the UML Class Diagram were implemented in the `/src` directory. Each class includes attributes and methods that match the system design.

### Creational Design Patterns
The following creational patterns were implemented in `/creational_patterns`:

- Simple Factory → Centralized movie creation
- Factory Method → Payment processing system
- Abstract Factory → UI component creation
- Builder → Step-by-step recommendation construction
- Prototype → Cloning movie objects
- Singleton → Single database connection instance

### Testing
Unit tests were created in the `/tests` directory using pytest.

The tests verify:
- Correct object creation
- Proper behavior of design patterns
- System consistency

All tests passed successfully.

---

## Assignment 11

### Repository Pattern
The repository pattern was implemented to separate business logic from storage logic.

Generic repositories were used to reduce duplication and improve maintainability.

### In-Memory Storage
HashMap/Dictionary-based repositories were implemented for:
- Movies
- Users

### Abstraction Mechanism
A Repository Factory was implemented to support future database integration without changing service logic.

### Future-Proofing
The architecture supports adding:
- Database repositories
- File system repositories
- Cloud-based storage

---

## Assignment 12

### Service Layer
A dedicated service layer was implemented to handle business logic separately from repositories and API routes.

### REST API
A REST API was developed using FastAPI.

Implemented endpoints include:
- Fetch movies
- Create movies
- Checkout movies

### Swagger/OpenAPI
FastAPI automatically generates Swagger/OpenAPI documentation.

Swagger UI is available at:

```text
http://127.0.0.1:8000/docs
```

### Testing
Integration and service tests were implemented using:
- pytest
- FastAPI TestClient
- httpx

All tests executed successfully.

---
