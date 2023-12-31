import time
import random
from asyncio import run
import redis 


async def main():
    # test = RedisTest()
    # print(f'Data: {test.name}')

    redis_client = redis.Redis(host='127.0.0.1',port=6379,decode_responses=True)
    now = time.time()
    redis_client.publish('Creep',f'yura loh at {now}')
    print(f'Sent data at: {now}')

    redis_sub = redis_client.pubsub()
    redis_sub.subscribe('Creep')

    for message in redis_sub.listen():
        print(f"Got data: {message} at {time.time()}")

run(main())