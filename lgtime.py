# 转换时间
import time
import datetime
# 当前时间戳1462696938.9103558
ticks = time.time()

''' 13位时间戳'''
ticks13 = int(ticks*1000)
print('当前时间戳:', ticks)
print('13位时间戳:', ticks13)

''' 将13位时间戳转换为当前时间'''
local_str_time1 = datetime.datetime.fromtimestamp(ticks13 / 1000.0)
print('local_str_tme1:', local_str_time1)


# 当前时间，年月日时分秒
localtime = time.localtime(time.time())
print('本地时间:', localtime)

# 格式化时间Sun May  8 16:42:18 2016
localtime1 = time.asctime(localtime)
print('本地时间格式化:', localtime1)

# 2016-05-08 16:42:18
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))


# 获取日历
import calendar
cal = calendar.month(2016, 5)
print('以下输出2016年5月日历:')
print(cal)

# t = 1462697335.845
# secs = time.mktime(t)
# secs1 = time.mktime(t)
# print('time.mktime(t): %f' % secs)
# print('asctime(localtime(secs)):%s' % time.asctime(time.localtime(secs)))

import datetime


'''将13位的时间戳转化为本地普通时间str类型：2016-05-08 16:48:55.845000'''
timestamp = 1462697335845
local_str_time = datetime.datetime.fromtimestamp(timestamp / 1000.0)


print('local_str_tme:', local_str_time)




'''将13位的时间戳转化为本地普通时间datetime类型：2016-05-08 16:48:55.845000'''
local_dt_time = datetime.datetime.fromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')
print('local_dt_time:', local_dt_time)

#
# local_timestamp = (time.mktime(localtime)*1000.0 + localtime.microseconds/1000.0)
#
# # local_timestamp = long(time.mktime(datetime_obj.timetuple()) * 1000.0 + datetime_obj.microsecond / 1000.0)
# print(local_timestamp)




#
#
# import time
# import datetime
#
#
# def timestamp_to_strtime(timestamp):
# 	''' 将13位整数的毫秒时间戳转化成本地普通时间（字符串格式） '''
# 	local_str_time = datetime.datetime.fromtimestamp(timestamp/1000.0)
# 	return local_str_time
#
# def timestamp_to_datetime(timestamp):
# 	''' 将13位毫秒时间戳转化成本地普通时间（datetime型）'''
# 	local_dt_time = datetime.datetime.fromtimestamp(timestamp/1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')
# 	return local_dt_time
# def datetime_to_strtime(datetime_obj):
# 	''' 将datetime格式的时间（含毫秒）转化成字符串'''
# 	local_str_time = datetime_obj.strftime('%Y-%m-%d %H:%M:%S.%f')
# 	return local_str_time
# def datetime_to_timestamp(datetime_obj):
# 	'''将本地(local) datetime 格式的时间 (含毫秒) 转为毫秒时间戳'''
# 	local_timestamp = long(time.mktime(datetime_obj.timetuple()) * 1000.0 + datetime_obj.microsecond / 1000.0)
# 	return local_timestamp
# def strtime_to_datetime(timestr):
# 	'''将字符串格式的时间 (含毫秒) 转为 datetiem 格式'''
# 	local_datetime = datetime.datetime.strftime(timestr, "%Y-%m-%d %H:%M:%S.%f")
# 	return local_datetime
# def strtime_to_timestamp(local_timestr):
# 	'''将本地时间 (字符串格式，含毫秒) 转为 13 位整数的毫秒时间戳'''
# 	local_datetime = strtime_to_datetime(local_timestr)
# 	timestamp = datetime_to_timestamp(local_datetime)
# 	return timestamp
#
#
#
#
# def current_datetime():
# 	'''返回本地当前时间, 包含datetime 格式, 字符串格式, 时间戳格式'''
#
# 	# 当前时间：datetime格式
# 	local_datetime_now = datetime.datetime.now()
# 	# 当前时间：字符串格式
# 	local_strtime_now = datetime_to_strtime(local_datetime_now)
# 	# 当前时间：时间戳格式 13位整数
# 	local_timestamp_now = datetime_to_timestamp(local_datetime_now)
# 	return local_datetime_now, local_strtime_now, local_timestamp_now
#
#
#
# if __name__ == '__main__':
# 	time_str = '2016-05-08 17:55:04.242'
#
# 	timestamp1 = strtime_to_timestamp(time_str)
# 	datetime1 = strtime_to_datetime(time_str)
#
# 	time_str2 = datetime_to_strtime(datetime1)
# 	timestamp2 = datetime_to_timestamp(datetime1)
#
# 	datetime3 = timestamp_to_datetime(timestamp2)
# 	time_str3 = timestamp_to_strtime(timestamp2)
#
# 	current_time = current_datetime()
#
#
# 	print('timestamp1:', timestamp1)
# 	print('datetime1:', datetime1)
# 	print('time_str2:', time_str2)
# 	print('timestamp2:', timestamp2)
# 	print('datetime3:', datetime3)
# 	print('time_str3:', time_str3)
