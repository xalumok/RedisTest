import redis 
import time
from asyncio import run

class RedisPublisher:

    def __init__(self) -> None:
        
        message = str(input("Enter publisher's message: "))
        self.redis_client = redis.Redis(host='127.0.0.1',port=6379,decode_responses=True)
        
        for i in range(0,100):
            self.redis_client.publish('Creep', f'{message}[{i}]')
            print(f'Sent message {message} at: {time.time()}')

async def main():
    pub = RedisPublisher()