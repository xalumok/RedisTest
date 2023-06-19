import redis 
import time
from asyncio import run
import asyncio

class RedisPublisher:

    def __init__(self) -> None:
        
        self.message = str(input("Enter publisher's message: "))
        self.redis_client = redis.Redis(host='127.0.0.1',port=6379,decode_responses=True)
        
    async def spam(self):
        while(True):

            for i in range(0,100):
                self.redis_client.publish('Creep', f'{self.message}[{i}]')
                print(f'Sent message {self.message} at: {time.time()}')
            await asyncio.sleep(3)

async def main():
    pub = RedisPublisher()
    await pub.spam()

run(main())