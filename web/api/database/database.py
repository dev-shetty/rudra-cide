

import redis

class Redis:
    def __init__(self):
        self.db = redis.Redis(host='localhost', port=6379, db=0)

    def set(self, key, value):
        self.r.set(key, value)

    def get(self, key):
        return self.r.get(key).decode()