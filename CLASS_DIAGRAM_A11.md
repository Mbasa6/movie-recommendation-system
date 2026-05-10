# Class Diagram for Assignment 11

```mermaid
classDiagram

class Repository {
    +save(obj)
    +find_by_id(id)
    +find_all()
    +delete(id)
}

class MovieRepository
class UserRepository

class InMemoryMovieRepository
class InMemoryUserRepository

class RepositoryFactory

Repository <|-- MovieRepository
Repository <|-- UserRepository

MovieRepository <|-- InMemoryMovieRepository
UserRepository <|-- InMemoryUserRepository

RepositoryFactory --> InMemoryMovieRepository
RepositoryFactory --> InMemoryUserRepository
```

---

## Explanation

The updated class diagram introduces the Repository Pattern into the system architecture.

### Key Design Decisions

- A generic Repository interface was used to define CRUD operations.
- Entity-specific repositories extend the generic repository.
- In-memory implementations store objects using Python dictionaries.
- A RepositoryFactory abstracts repository creation.

### Benefits

- Reduces code duplication
- Improves scalability
- Simplifies maintenance
- Supports future database integration