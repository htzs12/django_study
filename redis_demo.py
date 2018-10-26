from redis import Redis


cache = Redis(host='127.0.0.1',port=6379)

# 操作字符串
cache.set('username','haogege')
print(cache.get('username'))

# b'haogege'



