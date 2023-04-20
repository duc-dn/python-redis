import redis

class RedisConnector:
    def __init__(self, host: str='localhost', port: str='6379', db: str='0'):
        self.host = host
        self.port = port
        self.db = db
    
    def _connect_redis(self):
        return (
            redis.Redis(
                host=self.host,
                port=self.port,
                db=self.db
            )
        )

    def insert_value(self, conn: str):
        try:
            for i in range(1, 10000):
                conn.hset('prime', i, i ** 2)
            print('Sucess')
        except Exception as e:
            print(f'Error: {e}')

    def get_prime(self, val: str, tname: str='prime'):
        conn = self._connect_redis()
        value = conn.hget(tname, val)
        return value

if __name__ == '__main__':
    r = RedisConnector()
    conn = r._connect_redis()

    r.insert_value(conn=conn)

