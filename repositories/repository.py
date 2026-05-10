class Repository:

    def save(self, obj):
        raise NotImplementedError

    def find_by_id(self, obj_id):
        raise NotImplementedError

    def find_all(self):
        raise NotImplementedError

    def delete(self, obj_id):
        raise NotImplementedError