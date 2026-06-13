class ContextStore:
    def __init__(self):
        self._data = {}

    def save(self, user_id, key, value):
        if user_id not in self._data:
            self._data[user_id] = []
        existing = [item for item in self._data[user_id] if item["key"] == key]
        if existing:
            existing[0]["value"] = value
        else:
            self._data[user_id].append({"key": key, "value": value})
        return True

    def list_for_user(self, user_id):
        return self._data.get(user_id, [])
