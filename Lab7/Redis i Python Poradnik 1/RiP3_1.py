from redis import Redis

redis_connection = Redis(decode_responses=True)

list_key ="example-list"

redis_connection.rpush(list_key,1,2,3,4,5)

print(redis_connection.lrange(list_key,1, 3))