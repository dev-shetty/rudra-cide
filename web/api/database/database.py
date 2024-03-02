

import redis
from config import REDIS_HOST, REDIS_PORT, REDIS_DB

class Redis:
    def __init__(self):
        self.db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

    def set(self, key, value):
        self.db.set(key, value)

    def get(self, key):
        return self.db.get(key)


# rdb = Redis()
# rdb.set('key', 'value')
# print(rdb.get('key'))
