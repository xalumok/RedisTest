import time
import redis
from asyncio import run

class RedisSubscriber:

    def __init__(self) -> None:

        redis_pub = redis.Redis(host='127.0.0.1',port=6379,decode_responses=True)
        
        redis_sub = redis_pub.pubsub()
        redis_sub.subscribe('Creep')
        #print(f'Subscribed at: {time.time()}')

        for message in redis_sub.listen():
            print(f"Got message. delay: {time.time() - float(message['Data'])}")

def main():
    sub = RedisSubscriber()

run(main())