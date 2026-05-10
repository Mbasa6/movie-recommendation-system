from repositories.user_repository import UserRepository

class InMemoryUserRepository(UserRepository):

    def __init__(self):
        self._storage = {}

    def save(self, user):
        self._storage[user.user_id] = user

    def find_by_id(self, user_id):
        return self._storage.get(user_id)

    def find_all(self):
        return list(self._storage.values())

    def delete(self, user_id):
        if user_id in self._storage:
            del self._storage[user_id]