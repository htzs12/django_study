# import memcache
#
# mc = memcache.Client(['127.0.0.1:11211'],debug=True)

# mc.set('username','haogege',time=60)　＃　设置单个值

# mc.set_multi({'username':'haoge','age':'20'},time=120) # 设置多个值
#
# username = mc.get('username') # 获取数据
# print(username)
#
# username = mc.delete('username') # 删除数据
# print(username)
#
# username = mc.get('username') # 获取数据
# print(username)

# mc.set('age',20,time=120)

# mc.incr('age',delta=2) # 自增２
# age = mc.get('age')
# print(age)

# mc.decr('age',delta=2) # 自减２
# age = mc.get('age')
# print(age)