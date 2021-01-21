from redis import Redis

redis_connection = Redis(decode_responses=True, db=0)


script ="""
local arr = {}
for i = 0, 10 do
    arr[i] = i
end
return arr
"""

print(redis_connection.eval(script,0))# lista od 1 do 10