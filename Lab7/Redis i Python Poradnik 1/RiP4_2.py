from redis import Redis

redis_connection = Redis(decode_responses=True)

redis_connection.zadd("sorted_set_key",{"key2": 1})
redis_connection.zadd("sorted_set_key",{"key1": 1})
redis_connection.zadd("sorted_set_key",{"key4": 1})
redis_connection.zadd("sorted_set_key",{"key3": 1})

print(redis_connection.zrange("sorted_set_key",0, -1,"withscores",True))